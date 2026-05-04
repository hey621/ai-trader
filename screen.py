#!/usr/bin/env python3
"""Polygon.io penny stock screener for PennyAlpha_Bot."""
import sys
import json
import urllib.request
from datetime import date, timedelta

import os
POLYGON_KEY = os.environ.get("POLYGON_KEY", "")
BASE = "https://api.polygon.io"

def get(path):
    sep = "&" if "?" in path else "?"
    url = f"{BASE}{path}{sep}apiKey={POLYGON_KEY}"
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read())

def screen():
    data = get("/v2/snapshot/locale/us/markets/stocks/gainers")
    candidates = []
    for t in data.get("tickers", []):
        price = t.get("day", {}).get("c", 0)
        prev_vol = t.get("prevDay", {}).get("v", 1) or 1
        day_vol = t.get("day", {}).get("v", 0)
        bid = t.get("lastQuote", {}).get("p", 0)
        ask = t.get("lastQuote", {}).get("P", 0)
        rvol = day_vol / prev_vol
        dollar_vol = price * day_vol
        spread = (ask - bid) / ask * 100 if ask > 0 else 99
        if 0.25 <= price <= 25.00 and rvol >= 1.2 and dollar_vol >= 100_000 and spread <= 5.0:
            candidates.append({
                "ticker": t["ticker"],
                "price": round(price, 2),
                "rvol": round(rvol, 1),
                "dollar_vol": round(dollar_vol),
                "spread": round(spread, 2),
                "bid": bid,
                "ask": ask,
            })
    return candidates

def technicals(ticker):
    today = date.today().isoformat()
    thirty_ago = (date.today() - timedelta(days=45)).isoformat()

    sma20_data = get(f"/v1/indicators/sma/{ticker}?timespan=day&window=20&series_type=close&limit=1")
    sma20 = sma20_data.get("results", {}).get("values", [{}])[0].get("value")

    sma50_data = get(f"/v1/indicators/sma/{ticker}?timespan=day&window=50&series_type=close&limit=1")
    sma50 = sma50_data.get("results", {}).get("values", [{}])[0].get("value")

    bars_data = get(f"/v2/aggs/ticker/{ticker}/range/1/day/{thirty_ago}/{today}?adjusted=true&sort=desc&limit=30")
    bars = bars_data.get("results", [])
    resistance = max((b["h"] for b in bars), default=None) if bars else None

    return {"sma20": sma20, "sma50": sma50, "resistance": resistance}

if __name__ == "__main__":
    candidates = screen()
    print(f"Found {len(candidates)} candidates passing price/RVOL/volume/spread filters:")
    for c in candidates:
        t = c["ticker"]
        tech = technicals(t)
        price = c["price"]
        above_sma20 = price > tech["sma20"] if tech["sma20"] else None
        above_sma50 = price > tech["sma50"] if tech["sma50"] else None
        resistance = tech["resistance"]
        upside = round((resistance - price) / price * 100, 1) if resistance else None
        score = sum([
            bool(above_sma20),
            bool(above_sma50),
            c["rvol"] > 3.0,
            bool(upside and upside >= 15),
        ])
        print(json.dumps({
            "ticker": t,
            "price": price,
            "rvol": c["rvol"],
            "dollar_vol": c["dollar_vol"],
            "spread": c["spread"],
            "sma20": round(tech["sma20"], 2) if tech["sma20"] else None,
            "above_sma20": above_sma20,
            "resistance": round(resistance, 2) if resistance else None,
            "upside_pct": upside,
            "tech_score": score,
        }))
