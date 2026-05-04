#!/usr/bin/env python3
# Run locally: .venv/bin/python3 trade.py  (after setting ALPACA_API_KEY / ALPACA_SECRET_KEY)
"""Read Monday BUY signals from TRADES.md and place Alpaca bracket orders."""
import os
import re
import math
import sys
from datetime import date

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import (
    MarketOrderRequest, StopLossRequest, TakeProfitRequest,
)
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest

API_KEY = os.environ.get("ALPACA_API_KEY", "")
SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY", "")

BUDGET_BY_CONVICTION = {"HIGH": 150.00, "MED": 100.00, "LOW": 75.00}
DEFAULT_BUDGET = 100.00
STOP_PCT = 0.10
DEFAULT_TARGET_PCT = 0.20
MAX_POSITIONS = 5

trading = TradingClient(API_KEY, SECRET_KEY, paper=True)
data = StockHistoricalDataClient(API_KEY, SECRET_KEY)


def parse_buy_signals(md: str) -> list[dict]:
    signals = []
    in_signals = False
    for line in md.splitlines():
        if "## EXECUTION QUEUE" in line:
            in_signals = True
            continue
        if in_signals and line.startswith("##"):
            break
        if in_signals and line.startswith("|") and "---" not in line and "Ticker" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 3 and cols[0] and cols[0] != "—":
                ticker = cols[0]
                signal = cols[1] if len(cols) > 1 else ""
                entry_str = re.sub(r"[^\d.]", "", cols[2]) if len(cols) > 2 else ""
                stop_str = re.sub(r"[^\d.]", "", cols[3]) if len(cols) > 3 else ""
                target_str = re.sub(r"[^\d.]", "", cols[4]) if len(cols) > 4 else ""
                conviction_raw = cols[5].upper() if len(cols) > 5 else ""
                if signal.upper() == "BUY" and ticker:
                    if "HIGH" in conviction_raw:
                        conv = "HIGH"
                    elif "LOW" in conviction_raw:
                        conv = "LOW"
                    else:
                        conv = "MED"
                    signals.append({
                        "ticker": ticker,
                        "entry_target": float(entry_str) if entry_str else None,
                        "stop_loss": float(stop_str) if stop_str else None,
                        "target": float(target_str) if target_str else None,
                        "conviction": conv,
                    })
    return signals


def parse_active_tickers(md: str) -> set[str]:
    tickers = set()
    in_section = False
    for line in md.splitlines():
        if "## ACTIVE POSITIONS" in line:
            in_section = True
            continue
        if in_section and line.startswith("##"):
            break
        if in_section and line.startswith("|") and "---" not in line and "Ticker" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if cols[0] and cols[0] != "—":
                tickers.add(cols[0])
    return tickers


def get_ask_price(ticker: str) -> float | None:
    try:
        req = StockLatestQuoteRequest(symbol_or_symbols=ticker)
        quote = data.get_stock_latest_quote(req)
        return float(quote[ticker].ask_price)
    except Exception as e:
        print(f"  Could not get quote for {ticker}: {e}")
        return None


def place_bracket_order(ticker: str, shares: int, stop: float, target: float) -> object | None:
    try:
        req = MarketOrderRequest(
            symbol=ticker,
            qty=shares,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY,
            order_class=OrderClass.BRACKET,
            stop_loss=StopLossRequest(stop_price=round(stop, 2)),
            take_profit=TakeProfitRequest(limit_price=round(target, 2)),
        )
        return trading.submit_order(req)
    except Exception as e:
        print(f"  Order failed for {ticker}: {e}")
        return None


def clear_execution_queue(md: str) -> str:
    """Replace EXECUTION QUEUE table rows with a blank placeholder."""
    lines = md.splitlines()
    result = []
    in_queue = False
    for line in lines:
        if "## EXECUTION QUEUE" in line:
            in_queue = True
            result.append(line)
            continue
        if in_queue and line.startswith("##"):
            in_queue = False
        if in_queue and line.startswith("|") and "---" not in line and "Ticker" not in line:
            continue  # drop data rows
        result.append(line)
    return "\n".join(result)


def update_active_positions(md: str, new_rows: list[str]) -> str:
    lines = md.splitlines()
    result = []
    in_section = False
    table_started = False
    inserted = False

    for line in lines:
        if "## ACTIVE POSITIONS" in line:
            in_section = True
            result.append(line)
            continue
        if in_section and not inserted:
            if line.startswith("|") and "---" not in line and "Ticker" not in line:
                table_started = True
            if table_started and not line.startswith("|"):
                for row in new_rows:
                    result.append(row)
                inserted = True
            if in_section and line.startswith("##") and not line.startswith("## ACTIVE"):
                if not inserted:
                    for row in new_rows:
                        result.append(row)
                    inserted = True
                in_section = False
        result.append(line)

    if not inserted:
        for row in new_rows:
            result.append(row)

    return "\n".join(result)


def main():
    with open("TRADES.md") as f:
        md = f.read()

    signals = parse_buy_signals(md)
    if not signals:
        print("No BUY signals found in TRADES.md.")
        sys.exit(0)

    active_tickers = parse_active_tickers(md)
    try:
        alpaca_positions = {p.symbol for p in trading.get_all_positions()}
    except Exception:
        alpaca_positions = set()

    all_held = alpaca_positions | active_tickers
    slots_available = MAX_POSITIONS - len(all_held)

    print(f"BUY signals: {[s['ticker'] for s in signals]}")
    print(f"Currently held: {all_held or 'none'}")
    print(f"Slots available: {slots_available}/{MAX_POSITIONS}")

    if slots_available <= 0:
        print("No slots available — already at max 5 positions.")
        sys.exit(0)

    new_rows = []
    placed = 0

    for sig in signals:
        if placed >= slots_available:
            break
        ticker = sig["ticker"]
        if ticker in all_held:
            print(f"  {ticker}: already held, skipping.")
            continue

        ask = get_ask_price(ticker)
        if ask is None:
            if sig["entry_target"]:
                ask = sig["entry_target"]
                print(f"  {ticker}: live quote unavailable, using researched entry ${ask:.2f}")
            else:
                continue
        if not (0.25 <= ask <= 25.00):
            print(f"  {ticker}: ask ${ask:.2f} out of range, skipping.")
            continue

        budget = BUDGET_BY_CONVICTION.get(sig["conviction"], DEFAULT_BUDGET)
        shares = math.floor(budget / ask)
        if shares < 1:
            print(f"  {ticker}: budget ${budget:.0f} too small for ask ${ask:.2f}, skipping.")
            continue

        stop = sig["stop_loss"] or round(ask * (1 - STOP_PCT), 2)
        target = sig["target"] or round(ask * (1 + DEFAULT_TARGET_PCT), 2)

        deployed = round(shares * ask, 2)
        print(f"  Placing {shares} shares of {ticker} @ ~${ask:.2f} "
              f"(${deployed:.0f}, {sig['conviction']}) | stop=${stop:.2f} target=${target:.2f}")

        order = place_bracket_order(ticker, shares, stop, target)
        if order:
            today = date.today().isoformat()
            row = (f"| {ticker} | ${ask:.2f} | {today} | ${deployed:.0f} | {shares} "
                   f"| — | — | Active | ${stop:.2f} | ${target:.2f} |")
            new_rows.append(row)
            print(f"    Bracket order submitted: {order.id}")
            placed += 1
        else:
            print(f"  {ticker}: order failed.")

    md_out = clear_execution_queue(md)
    if new_rows:
        md_out = update_active_positions(md_out, new_rows)
        print(f"\nPlaced {placed} order(s).")
    else:
        print("\nNo new orders placed.")
    with open("TRADES.md", "w") as f:
        f.write(md_out)
    print("TRADES.md updated.")


if __name__ == "__main__":
    main()
