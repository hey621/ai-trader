#!/usr/bin/env python3
"""Check ACTIVE POSITIONS against current Polygon prices. Print alerts for stop loss / target hits."""
import json
import re
import urllib.request

POLYGON_KEY = "vTsb4KhgEMTkAigTlWOkKXr5xStlg_qV"
BASE = "https://api.polygon.io"

def get_price(ticker):
    url = f"{BASE}/v2/snapshot/locale/us/markets/stocks/tickers/{ticker}?apiKey={POLYGON_KEY}"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read())
        return data.get("ticker", {}).get("day", {}).get("c") or \
               data.get("ticker", {}).get("lastTrade", {}).get("p")
    except Exception:
        return None

def parse_positions(trades_md):
    """Extract active positions from TRADES.md. Returns list of dicts."""
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
                stop_str  = re.sub(r"[^\d.]", "", cols[7]) if len(cols) > 7 else ""
                try:
                    entry = float(entry_str)
                    stop  = float(stop_str) if stop_str else entry * 0.90
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
        raise SystemExit(0)

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
            alerts.append(f"STOP LOSS HIT: {p['ticker']} now ${price:.2f} ({pct:+.1f}%) — entry was ${p['entry']:.2f}, stop was ${p['stop']:.2f}")
        elif price >= p["target"]:
            status = "TARGET_HIT"
            alerts.append(f"TARGET HIT: {p['ticker']} now ${price:.2f} ({pct:+.1f}%) — entry was ${p['entry']:.2f}, target was ${p['target']:.2f}")
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
