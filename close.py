#!/usr/bin/env python3
# Run locally: .venv/bin/python3 close.py  (after setting ALPACA_API_KEY / ALPACA_SECRET_KEY)
"""Check Alpaca positions for stop/target hits and close them. Updates TRADES.md."""
import os
import re
import sys
from datetime import date

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import ClosePositionRequest
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestTradeRequest

API_KEY = os.environ.get("ALPACA_API_KEY", "")
SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY", "")

trading = TradingClient(API_KEY, SECRET_KEY, paper=True)
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)


def get_price(ticker: str) -> float | None:
    try:
        req = StockLatestTradeRequest(symbol_or_symbols=ticker)
        trade = data_client.get_stock_latest_trade(req)
        return float(trade[ticker].price)
    except Exception:
        return None


def parse_positions(md: str) -> list[dict]:
    positions = []
    in_section = False
    for line in md.splitlines():
        if "## ACTIVE POSITIONS" in line:
            in_section = True
            continue
        if in_section and line.startswith("##"):
            break
        if in_section and line.startswith("|") and "---" not in line and "Ticker" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 2 and cols[0] and cols[0] != "—":
                ticker = cols[0]
                entry_str = re.sub(r"[^\d.]", "", cols[1]) if len(cols) > 1 else ""
                stop_str = re.sub(r"[^\d.]", "", cols[7]) if len(cols) > 7 else ""
                try:
                    entry = float(entry_str)
                    stop = float(stop_str) if stop_str else entry * 0.90
                    target = entry * 1.20
                    positions.append({"ticker": ticker, "entry": entry, "stop": stop, "target": target, "raw": line})
                except ValueError:
                    pass
    return positions


def move_to_closed(md: str, ticker: str, entry: float, exit_price: float, result: str) -> str:
    today = date.today().isoformat()
    eligible = (date.today().replace(year=date.today().year + 1) if False else  # placeholder
                date.fromisoformat(today).replace(day=date.fromisoformat(today).day))
    # Eligible again = 30 days from today
    from datetime import timedelta
    eligible_date = (date.today() + timedelta(days=30)).isoformat()

    lines = md.splitlines()
    result_lines = []
    in_active = False
    skip_ticker = False

    for line in lines:
        if "## ACTIVE POSITIONS" in line:
            in_active = True
            result_lines.append(line)
            continue
        if in_active and line.startswith("##"):
            in_active = False
        if in_active and line.startswith("|") and "---" not in line and "Ticker" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if cols[0] == ticker:
                skip_ticker = True
                continue
        result_lines.append(line)

    closed_row = f"| {ticker} | ${entry:.2f} | ${exit_price:.2f} | {result} | {today} | {eligible_date} |"
    out = []
    for line in result_lines:
        out.append(line)
        if "## CLOSED TRADES" in line:
            pass
        if line.startswith("| —") and "## CLOSED" not in line:
            pass
    # Insert into CLOSED TRADES
    final = []
    in_closed = False
    inserted = False
    for line in out:
        if "## CLOSED TRADES" in line:
            in_closed = True
            final.append(line)
            continue
        if in_closed and not inserted and line.startswith("|") and "---" not in line and "Ticker" not in line:
            final.append(closed_row)
            inserted = True
        if in_closed and line.startswith("##") and "CLOSED" not in line:
            if not inserted:
                final.append(closed_row)
                inserted = True
            in_closed = False
        final.append(line)
    if not inserted:
        final.append(closed_row)

    return "\n".join(final)


def main():
    with open("TRADES.md") as f:
        md = f.read()

    positions = parse_positions(md)
    if not positions:
        print("NO_ACTIVE_POSITIONS")
        sys.exit(0)

    try:
        alpaca_positions = {p.symbol: p for p in trading.get_all_positions()}
    except Exception as e:
        print(f"Could not fetch Alpaca positions: {e}")
        sys.exit(1)

    closed_any = False
    for p in positions:
        ticker = p["ticker"]
        price = get_price(ticker)
        if price is None:
            print(f"{ticker}: price unavailable, skipping.")
            continue

        pct = (price - p["entry"]) / p["entry"] * 100
        reason = None
        result = None

        if price <= p["stop"]:
            reason = f"STOP LOSS ({pct:+.1f}%)"
            result = "LOSS"
        elif price >= p["target"]:
            reason = f"TARGET HIT ({pct:+.1f}%)"
            result = "WIN"

        if reason:
            print(f"{ticker}: ${price:.2f} — {reason}. Closing position...")
            if ticker in alpaca_positions:
                try:
                    trading.close_position(ticker)
                    print(f"  Closed on Alpaca.")
                except Exception as e:
                    print(f"  Alpaca close failed: {e}")
            else:
                print(f"  Not found in Alpaca positions — marking closed in TRADES.md only.")
            md = move_to_closed(md, ticker, p["entry"], price, result)
            closed_any = True
        else:
            print(f"{ticker}: ${price:.2f} ({pct:+.1f}%) — holding.")

    if closed_any:
        with open("TRADES.md", "w") as f:
            f.write(md)
        print("\nTRADES.md updated.")
    else:
        print("\nALL_CLEAR: No positions closed.")


if __name__ == "__main__":
    main()
