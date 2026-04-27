#!/usr/bin/env python3
"""Check ACTIVE POSITIONS against current prices. Trail stop as positions move up. Print alerts."""
import os
import re
import sys

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest, ReplaceOrderRequest
from alpaca.trading.enums import QueryOrderStatus, OrderSide, OrderType
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestTradeRequest

API_KEY = os.environ.get("ALPACA_API_KEY", "")
SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY", "")

STOP_PCT = 0.10
DEFAULT_TARGET_PCT = 0.20

# Trailing stop steps: (price_gain_pct, raise_stop_to_pct_of_entry)
# e.g. if up 10%, move stop to breakeven (0%); if up 20%, lock in +10%
TRAIL_STEPS = [(0.20, 0.10), (0.10, 0.00)]

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
    """Columns: Ticker|Entry|Date|Deployed|Shares|CurPrice|P&L$|P&L%|Stop|Target|Status"""
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
            if len(cols) >= 2 and cols[0] and cols[0] != "—":
                ticker = cols[0]
                entry_str = re.sub(r"[^\d.]", "", cols[1]) if len(cols) > 1 else ""
                stop_str = re.sub(r"[^\d.]", "", cols[8]) if len(cols) > 8 else ""
                target_str = re.sub(r"[^\d.]", "", cols[9]) if len(cols) > 9 else ""
                try:
                    entry = float(entry_str)
                    stop = float(stop_str) if stop_str else round(entry * (1 - STOP_PCT), 2)
                    target = float(target_str) if target_str else round(entry * (1 + DEFAULT_TARGET_PCT), 2)
                    positions.append({"ticker": ticker, "entry": entry, "stop": stop, "target": target})
                except ValueError:
                    pass
    return positions


def find_stop_order(ticker: str):
    """Find the open stop-loss order for a ticker on Alpaca."""
    try:
        orders = trading.get_orders(filter=GetOrdersRequest(
            symbols=[ticker],
            status=QueryOrderStatus.OPEN,
            side=OrderSide.SELL,
        ))
        for o in orders:
            if o.order_type in (OrderType.STOP, OrderType.STOP_LIMIT):
                return o
    except Exception:
        pass
    return None


def raise_stop(ticker: str, new_stop: float, old_stop: float) -> bool:
    """Replace the open stop order with a higher stop price. Returns True if successful."""
    order = find_stop_order(ticker)
    if order is None:
        print(f"  {ticker}: could not find open stop order to trail.")
        return False
    try:
        trading.replace_order_by_id(str(order.id), ReplaceOrderRequest(stop_price=round(new_stop, 2)))
        print(f"  {ticker}: trailed stop ${old_stop:.2f} → ${new_stop:.2f}")
        return True
    except Exception as e:
        print(f"  {ticker}: failed to replace stop order: {e}")
        return False


def update_stop_in_md(md: str, ticker: str, new_stop: float) -> str:
    """Update the stop column (col 8) for a ticker in ACTIVE POSITIONS."""
    lines = md.splitlines()
    result = []
    in_active = False
    for line in lines:
        if "## ACTIVE POSITIONS" in line:
            in_active = True
            result.append(line)
            continue
        if in_active and line.startswith("##"):
            in_active = False
        if in_active and line.startswith("|") and "---" not in line and "Ticker" not in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if cols[0] == ticker and len(cols) > 8:
                cols[8] = f"${new_stop:.2f}"
                result.append("| " + " | ".join(cols) + " |")
                continue
        result.append(line)
    return "\n".join(result)


if __name__ == "__main__":
    with open("TRADES.md") as f:
        md = f.read()

    positions = parse_positions(md)
    if not positions:
        print("NO_ACTIVE_POSITIONS")
        sys.exit(0)

    alerts = []
    updates = []
    md_dirty = False

    for p in positions:
        price = get_price(p["ticker"])
        if price is None:
            updates.append(f"{p['ticker']}: price unavailable")
            continue

        pct = (price - p["entry"]) / p["entry"] * 100
        status = "OK"

        if price <= p["stop"]:
            status = "STOP_HIT"
            alerts.append(
                f"STOP LOSS HIT: {p['ticker']} now ${price:.2f} ({pct:+.1f}%) "
                f"— entry ${p['entry']:.2f}, stop ${p['stop']:.2f}"
            )
        elif price >= p["target"]:
            status = "TARGET_HIT"
            alerts.append(
                f"TARGET HIT: {p['ticker']} now ${price:.2f} ({pct:+.1f}%) "
                f"— entry ${p['entry']:.2f}, target ${p['target']:.2f}"
            )
        else:
            # Check trailing stop steps (highest gain first)
            for gain_threshold, new_stop_pct in TRAIL_STEPS:
                new_stop = round(p["entry"] * (1 + new_stop_pct), 2)
                if pct / 100 >= gain_threshold and p["stop"] < new_stop:
                    if raise_stop(p["ticker"], new_stop, p["stop"]):
                        md = update_stop_in_md(md, p["ticker"], new_stop)
                        md_dirty = True
                        updates.append(
                            f"{p['ticker']}: ${price:.2f} ({pct:+.1f}%) "
                            f"[STOP TRAILED → ${new_stop:.2f}]"
                        )
                    break
            else:
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

    if md_dirty:
        with open("TRADES.md", "w") as f:
            f.write(md)
        print("\nTRADES.md updated with trailed stops.")
