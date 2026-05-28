# Crypto Market Data Pipeline

## Objective

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using the CoinGecko public API and Google BigQuery.

The pipeline fetches cryptocurrency market data, transforms it into a structured tabular format, generates analytical insights, and stores the processed data inside BigQuery for querying and analysis.

---

# API Chosen

## CoinGecko API

The CoinGecko API was selected because:
- it is free to use
- no API key is required
- it provides structured JSON responses
- cryptocurrency market data is suitable for analytics use cases

---

# Pipeline Architecture

```text
CoinGecko API
       ↓
Fetch Raw JSON Data
       ↓
Transform and Clean Data
       ↓
Generate Derived Fields
       ↓
Load into BigQuery
       ↓
Run SQL Analysis
```

---

# Technologies Used

- Python
- requests
- pandas
- Google BigQuery
- Google Cloud Service Accounts

---

# Features Implemented

## Data Fetching
- Retrieves live cryptocurrency market data
- Handles API failures using exception handling
- Includes logging for monitoring execution

## Data Transformation
- Flattens nested JSON data
- Converts API response into tabular structure
- Handles missing values safely
- Adds derived analytical field:
  - market_trend

## BigQuery Integration
- Loads transformed data into BigQuery
- Uses structured schema and appropriate data types

---

# Derived Field Logic

The pipeline generates a custom analytical field called `market_trend`.

Logic:
- change > 5 → Bullish
- change < -5 → Bearish
- otherwise → Stable

This adds analytical value beyond the raw API response.

---

# How to Run the Pipeline

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Pipeline

```bash
python main.py
```

---

# BigQuery Setup

1. Create a Google Cloud project
2. Enable BigQuery Sandbox
3. Create dataset:
   - crypto_pipeline
4. Create service account with BigQuery permissions
5. Download JSON credentials
6. Store credentials locally as:
   - service_account.json

---

# SQL Analysis

Example SQL query:

```sql
SELECT
    market_trend,
    COUNT(*) AS total_coins,
    AVG(change_24h) AS average_change
FROM `PROJECT_ID.crypto_pipeline.market_data`
GROUP BY market_trend
ORDER BY average_change DESC;
```

The query summarizes market movement trends across the loaded cryptocurrency data.

---

# Production Considerations

## Scheduling

The pipeline could be scheduled using:
- Cloud Scheduler
- cron jobs
- Apache Airflow

A daily scheduled run would be sufficient for this use case.

---

## Monitoring and Failure Detection

Production improvements would include:
- centralized logging
- email alerts on failure
- retry mechanisms
- monitoring dashboards

---

## Scaling to Larger Data Volumes

If the pipeline needed to scale significantly:
- asynchronous API requests could be introduced
- BigQuery partitioned tables could improve performance
- orchestration tools such as Airflow could manage workflows
- Docker containers could standardize deployments

---

# Future Improvements

Potential future enhancements:
- support for additional cryptocurrencies
- historical trend analysis
- real-time streaming updates
- dashboard visualization layer
- automated anomaly detection
