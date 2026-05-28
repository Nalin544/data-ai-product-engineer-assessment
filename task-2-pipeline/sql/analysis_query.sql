SELECT
    market_trend,
    COUNT(*) AS total_coins,
    AVG(change_24h) AS average_change
FROM `crypto-market-pipeline-497618.crypto_pipeline.market_data`
GROUP BY market_trend
ORDER BY average_change DESC;