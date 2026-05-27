import requests
import logging

logging.basicConfig(level=logging.INFO)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,solana"
}


def fetch_crypto_data():
    try:
        logging.info("Fetching cryptocurrency market data...")

        response = requests.get(API_URL, params=PARAMS, timeout=10)

        response.raise_for_status()

        data = response.json()

        logging.info("Data fetched successfully.")

        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return []