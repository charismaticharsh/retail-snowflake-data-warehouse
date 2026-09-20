-- Snowflake Change Data Capture Demonstration
-- Create a Stream on the staging orders table.
-- The Stream captures changes made after its offset is established.

CREATE OR REPLACE STREAM RETAIL_DWH.STAGING.STG_ORDERS_STREAM
ON TABLE RETAIL_DWH.STAGING.STG_ORDERS;

-- Verify the Stream
SHOW STREAMS IN SCHEMA RETAIL_DWH.STAGING;

-- View captured changes
SELECT *
FROM RETAIL_DWH.STAGING.STG_ORDERS_STREAM;

-- CDC DEMONSTRATION
-- Update an existing staging record to generate a CDC event.
-- Use an existing ORDER_ID from STG_ORDERS.

UPDATE RETAIL_DWH.STAGING.STG_ORDERS
SET ORDER_STATUS = 'CDC_TEST'
WHERE ORDER_ID = 1000001;

-- View the captured change.
SELECT *
FROM RETAIL_DWH.STAGING.STG_ORDERS_STREAM;


-- Stream metadata includes:
-- METADATA$ACTION
-- METADATA$ISUPDATE
-- METADATA$ROW_ID
