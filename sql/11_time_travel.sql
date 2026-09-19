-- Snowflake Time Travel
-- Retrieves the DIM_CUSTOMER table as it existed 5 minutes ago.
-- OFFSET => -300 means 300 seconds (5 minutes) before the current time.
-- LIMIT 10 returns only the first 10 rows for verification.

SELECT *
FROM RETAIL_DWH.CORE.DIM_CUSTOMER
AT (OFFSET => -60 * 5)
LIMIT 10;
