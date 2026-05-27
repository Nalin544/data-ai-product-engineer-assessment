import pandas as pd


def determine_market_trend(change):
    if change > 5:
        return "Bullish"
    elif change < -5:
        return "Bearish"
    else:
        return "Stable"


def transform_data(data):

    transformed = []

    for coin in data:

        transformed.append({
            "coin": coin.get("id"),
            "symbol": coin.get("symbol"),
            "current_price": coin.get("current_price"),
            "market_cap": coin.get("market_cap"),
            "total_volume": coin.get("total_volume"),
            "change_24h": coin.get("price_change_percentage_24h"),
            "market_trend": determine_market_trend(
                coin.get("price_change_percentage_24h", 0)
            )
        })

    df = pd.DataFrame(transformed)

    return df