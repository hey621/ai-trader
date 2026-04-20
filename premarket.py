#!/usr/bin/env python3
"""Pre-market scanner using Polygon. Screens for penny stocks with pre-market momentum."""
import json
import urllib.request
from datetime import date, timedelta

POLYGON_KEY = "vTsb4KhgEMTkAigTlWOkKXr5xStlg_qV"
BASE = "https://api.polygon.io"

def get(path):
    sep = "&" if "?" in path else "?"
    url = f"{BASE}{path}{sep}apiKey={POLYGON_KEY}"
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read())

def premarket_movers():
    """Get gainers snapshot — pre-market prices are reflected early Monday morning."""
    data = get("/v2/snapshot/locale/us/markets/stocks/gainers")
    candidates = []
    for t in data.get("tickers", []):
        # Use preMarket price if available, fall back to last close
        pm_price = t.get("day", {}).get("o") or t.get("prevDay", {}).get("c", 0)
        prev_close = t.get("prevDay", {}).get("c", 0)
        last_price = t.get("day", {}).get("c") or prev_close

        # Pre-market change vs previous close
        pm_change_pct = ((pm_price - prev_close) / prev_close * 100) if prev_close > 0 else 0

        prev_vol = t.get("prevDay", {}).get("v", 1) or 1
        day_vol = t.get("day", {}).get("v", 0)
        rvol = day_vol / prev_vol if day_vol else 0

        bid = t.get("lastQuote", {}).get("p", 0)
        ask = t.get("lastQuote", {}).get("P", 0)
        spread = (ask - bid) / ask * 100 if ask > 0 else 99

        dollar_vol = prev_close * prev_vol  # use prev day dollar vol as liquidity proxy

        if (0.50 <= prev_close <= 5.00
                and abs(pm_change_pct) >= 5.0   # at least 5% pre-market move
                and dollar_vol >= 500_000
                and spread <= 3.0):
            candidates.append({
                "ticker": t["ticker"],
                "prev_close": round(prev_close, 2),
                "pm_price": round(pm_price, 2),
                "pm_change_pct": round(pm_change_pct, 1),
                "prev_dollar_vol": round(dollar_vol),
                "spread": round(spread, 2),
                "rvol": round(rvol, 2),
                "direction": "UP" if pm_change_pct > 0 else "DOWN",
            })

    # Sort by absolute pre-market move, strongest first
    candidates.sort(key=lambda x: abs(x["pm_change_pct"]), reverse=True)
    return candidates

def get_sma(ticker, window=20):
    try:
        data = get(f"/v1/indicators/sma/{ticker}?timespan=day&window={window}&series_type=close&limit=1")
        return data.get("results", {}).get("values", [{}])[0].get("value")
    except Exception:
        return None

if __name__ == "__main__":
    movers = premarket_movers()
    print(f"Found {len(movers)} pre-market candidates (>=5% move, $0.50-$5.00, $500k+ liquidity):")
    for m in movers:
        sma20 = get_sma(m["ticker"])
        above_sma = m["prev_close"] > sma20 if sma20 else None
        print(json.dumps({**m, "sma20": round(sma20, 2) if sma20 else None, "above_sma20": above_sma}))
