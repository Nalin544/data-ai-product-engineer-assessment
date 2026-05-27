from fetch_data import fetch_crypto_data
from transform_data import transform_data


def main():

    raw_data = fetch_crypto_data()

    if not raw_data:
        print("No data received from API.")
        return

    transformed_df = transform_data(raw_data)

    print("\nTransformed Data:\n")
    print(transformed_df)


if __name__ == "__main__":
    main()