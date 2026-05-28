from google.cloud import bigquery
from google.oauth2 import service_account

PROJECT_ID = "crypto-market-pipeline-497618"
DATASET_ID = "crypto_pipeline"
TABLE_ID = "market_data"

credentials = service_account.Credentials.from_service_account_file(
    "service_account.json"
)


def load_data_to_bigquery(df):

    client = bigquery.Client(
        credentials=credentials,
        project=PROJECT_ID
    )

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    job = client.load_table_from_dataframe(df, table_ref)

    job.result()

    print(f"Loaded {len(df)} rows into BigQuery.")