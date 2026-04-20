#!/usr/bin/env python3
"""Check ACTIVE POSITIONS against current Alpaca prices. Print alerts for stop loss / target hits."""
import os
import re
import sys

from alpaca.trading.client import TradingClient
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


def parse_positions(trades_md: str) -> list[dict]:
    positions = []
    in_section = False
    for line in trades_md.splitlines():
        if "## ACTIVE POSITIONS" in line:
            in_section = True
            continue
        if in_section and line.startswith("##"):
            break
        if in_section and line.startswith("|") and "---" not in line and "Ticker" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 5 and cols[0] and cols[0] != "—":
                ticker = cols[0]
                entry_str = re.sub(r"[^\d.]", "", cols[1]) if len(cols) > 1 else ""
                stop_str = re.sub(r"[^\d.]", "", cols[7]) if len(cols) > 7 else ""
                try:
                    entry = float(entry_str)
                    stop = float(stop_str) if stop_str else entry * 0.90
                    target = entry * 1.20
                    positions.append({"ticker": ticker, "entry": entry, "stop": stop, "target": target})
                except ValueError:
                    pass
    return positions


if __name__ == "__main__":
    with open("TRADES.md") as f:
        md = f.read()

    positions = parse_positions(md)
    if not positions:
        print("NO_ACTIVE_POSITIONS")
        sys.exit(0)

    alerts = []
    updates = []
    for p in positions:
        price = get_price(p["ticker"])
        if price is None:
            updates.append(f"{p['ticker']}: price unavailable")
            continue
        pct = (price - p["entry"]) / p["entry"] * 100
        status = "OK"
        if price <= p["stop"]:
            status = "STOP_HIT"
            alerts.append(f"STOP LOSS HIT: {p['ticker']} now ${price:.2f} ({pct:+.1f}%) — entry ${p['entry']:.2f}, stop ${p['stop']:.2f}")
        elif price >= p["target"]:
            status = "TARGET_HIT"
            alerts.append(f"TARGET HIT: {p['ticker']} now ${price:.2f} ({pct:+.1f}%) — entry ${p['entry']:.2f}, target ${p['target']:.2f}")
        updates.append(f"{p['ticker']}: ${price:.2f} ({pct:+.1f}%) [{status}]")

    print("--- Position Check ---")
    for u in updates:
        print(u)

    if alerts:
        print("\n--- ALERTS ---")
        for a in alerts:
            print(a)
    else:
        print("\nALL_CLEAR: No stops or targets hit.")
