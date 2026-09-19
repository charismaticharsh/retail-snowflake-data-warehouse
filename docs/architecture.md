# Architecture

## End-to-End Flow

Python
↓
CSV / JSON
↓
Snowflake Stage
↓
RAW
↓
STAGING
↓
CORE
↓
DATA MART
↓
Analytics

## Data Layers

### RAW
Stores source data in its original form.

### STAGING
Cleans, standardizes and validates source data.

Structured CSV data is transformed into relational staging tables.

JSON customer events are loaded and parsed using Snowflake VARIANT functionality.

### CORE
Implements a dimensional Star Schema.

Dimensions:
- DIM_CUSTOMER
- DIM_PRODUCT
- DIM_STORE
- DIM_DATE

Facts:
- FACT_ORDER
- FACT_ORDER_ITEM
- FACT_CUSTOMER_EVENT

### DATA MART
Business-oriented analytical tables:

- DM_DAILY_SALES
- DM_PRODUCT_SALES
- DM_CUSTOMER_SALES
- DM_CUSTOMER_BEHAVIOR

**## Snowflake Feature**

- Snowflake Streams
- Snowflake Tasks
- Time Travel
- Zero-Copy Cloning
- VARIANT / JSON
- Window Functions
- Query History
