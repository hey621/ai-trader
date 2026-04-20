#!/usr/bin/env python3
# Run locally: .venv/bin/python3 trade.py  (after setting ALPACA_API_KEY / ALPACA_SECRET_KEY)
"""Read Monday BUY signals from TRADES.md and place Alpaca paper orders."""
import os
import re
import sys
from datetime import date

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest

API_KEY = os.environ.get("ALPACA_API_KEY", "")
SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY", "")
BUDGET_PER_POSITION = 100.00
MAX_POSITIONS = 5

trading = TradingClient(API_KEY, SECRET_KEY, paper=True)
data = StockHistoricalDataClient(API_KEY, SECRET_KEY)


def parse_buy_signals(md: str) -> list[dict]:
    signals = []
    in_signals = False
    for line in md.splitlines():
        if "## MONDAY SIGNALS" in line:
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
                if signal.upper() == "BUY" and ticker:
                    signals.append({
                        "ticker": ticker,
                        "entry_target": float(entry_str) if entry_str else None,
                        "stop_loss": float(stop_str) if stop_str else None,
                    })
    return signals


def parse_active_positions(md: str) -> list[str]:
    tickers = []
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
                tickers.append(cols[0])
    return tickers


def get_ask_price(ticker: str) -> float | None:
    try:
        req = StockLatestQuoteRequest(symbol_or_symbols=ticker)
        quote = data.get_stock_latest_quote(req)
        return float(quote[ticker].ask_price)
    except Exception as e:
        print(f"  Could not get quote for {ticker}: {e}")
        return None


def place_order(ticker: str, notional: float) -> dict | None:
    try:
        req = MarketOrderRequest(
            symbol=ticker,
            notional=round(notional, 2),
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY,
        )
        order = trading.submit_order(req)
        return order
    except Exception as e:
        print(f"  Order failed for {ticker}: {e}")
        return None


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
                result.append(line)
                continue
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

    active_tickers = parse_active_positions(md)
    # Also check actual Alpaca positions
    try:
        alpaca_positions = {p.symbol for p in trading.get_all_positions()}
    except Exception:
        alpaca_positions = set()

    slots_used = len(alpaca_positions) if alpaca_positions else len(active_tickers)
    slots_available = MAX_POSITIONS - slots_used

    print(f"BUY signals: {[s['ticker'] for s in signals]}")
    print(f"Alpaca positions: {alpaca_positions or active_tickers}")
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
        if ticker in alpaca_positions or ticker in active_tickers:
            print(f"  {ticker}: already in portfolio, skipping.")
            continue

        ask = get_ask_price(ticker)
        if ask is None:
            continue
        if not (0.50 <= ask <= 5.00):
            print(f"  {ticker}: ask ${ask:.2f} out of range, skipping.")
            continue

        print(f"  Placing ${BUDGET_PER_POSITION:.0f} BUY order for {ticker} @ ~${ask:.2f}...")
        order = place_order(ticker, BUDGET_PER_POSITION)
        if order:
            stop = sig["stop_loss"] or round(ask * 0.90, 2)
            today = date.today().isoformat()
            shares_approx = round(BUDGET_PER_POSITION / ask, 1)
            row = f"| {ticker} | ${ask:.2f} | {today} | ${BUDGET_PER_POSITION:.0f} | — | — | — | Active | stop=${stop:.2f} |"
            new_rows.append(row)
            print(f"    Order submitted: {order.id}")
            placed += 1
        else:
            print(f"  {ticker}: order failed.")

    if new_rows:
        md_updated = update_active_positions(md, new_rows)
        with open("TRADES.md", "w") as f:
            f.write(md_updated)
        print(f"\nPlaced {placed} order(s). TRADES.md updated.")
    else:
        print("\nNo new orders placed.")


if __name__ == "__main__":
    main()
