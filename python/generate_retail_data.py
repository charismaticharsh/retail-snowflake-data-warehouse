import os
import json
import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

# 1. CONFIGURATION
fake = Faker("en_IN")

# Makes generated data reproducible
random.seed(42)
Faker.seed(42)


# Find project root
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Data folder
DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

# Create data folder if it doesn't exist
os.makedirs(
    DATA_DIR,
    exist_ok=True
)


# Number of records
NUM_CUSTOMERS = 5000
NUM_PRODUCTS = 500
NUM_STORES = 20
NUM_ORDERS = 100000
NUM_EVENTS = 100000


# Date range
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2026, 8, 20)

# 2. HELPER FUNCTION
def random_date(start_date, end_date):

    delta = end_date - start_date

    random_days = random.randint(
        0,
        delta.days
    )

    return start_date + timedelta(
        days=random_days
    )

# 3. GENERATE CUSTOMERS
print()
print("Generating customers...")

customers = []

states = [
    "Rajasthan",
    "Delhi",
    "Maharashtra",
    "Karnataka",
    "Tamil Nadu",
    "Gujarat",
    "West Bengal",
    "Telangana",
    "Uttar Pradesh",
    "Haryana"
]

customer_types = [
    "REGULAR",
    "PREMIUM",
    "VIP"
]


for customer_id in range(
    1001,
    1001 + NUM_CUSTOMERS
):

    created_date = random_date(
        START_DATE,
        datetime(2026, 6, 30)
    )

    updated_date = random_date(
        created_date,
        END_DATE
    )

    first_name = fake.first_name()
    last_name = fake.last_name()

    customers.append({

        "CUSTOMER_ID": customer_id,

        "FIRST_NAME": first_name,

        "LAST_NAME": last_name,

        "EMAIL":
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{customer_id}@example.com",

        "PHONE":
            fake.msisdn()[:10],

        "CITY":
            fake.city(),

        "STATE":
            random.choice(states),

        "COUNTRY":
            "India",

        "CUSTOMER_TYPE":
            random.choice(customer_types),

        "CREATED_DATE":
            created_date,

        "UPDATED_DATE":
            updated_date
    })


customers_df = pd.DataFrame(
    customers
)


customers_df.to_csv(
    os.path.join(
        DATA_DIR,
        "customers.csv"
    ),
    index=False
)


print(
    f"Customers created: "
    f"{len(customers_df)}"
)

# 4. GENERATE PRODUCTS
print()
print("Generating products...")


categories = {

    "Electronics": [
        "Mobile",
        "Laptop",
        "Tablet",
        "Headphones"
    ],

    "Clothing": [
        "Shirts",
        "Jeans",
        "Shoes",
        "Jackets"
    ],

    "Home": [
        "Furniture",
        "Kitchen",
        "Decor",
        "Appliances"
    ],

    "Accessories": [
        "Watch",
        "Bags",
        "Wallet",
        "Sunglasses"
    ]
}


brands = [
    "Samsung",
    "Apple",
    "Sony",
    "Nike",
    "Adidas",
    "Puma",
    "LG",
    "Dell",
    "HP",
    "Lenovo"
]


products = []


for product_id in range(
    5001,
    5001 + NUM_PRODUCTS
):

    category = random.choice(
        list(categories.keys())
    )

    subcategory = random.choice(
        categories[category]
    )

    price = round(
        random.uniform(
            500,
            100000
        ),
        2
    )

    cost = round(
        price *
        random.uniform(
            0.55,
            0.85
        ),
        2
    )

    created_date = random_date(
        START_DATE,
        datetime(2026, 6, 30)
    )

    updated_date = random_date(
        created_date,
        END_DATE
    )

    products.append({

        "PRODUCT_ID":
            product_id,

        "PRODUCT_NAME":
            f"{subcategory} "
            f"Product {product_id}",

        "CATEGORY":
            category,

        "SUBCATEGORY":
            subcategory,

        "BRAND":
            random.choice(brands),

        "PRICE":
            price,

        "COST":
            cost,

        "SUPPLIER_ID":
            random.randint(
                9001,
                9050
            ),

        "STOCK_QUANTITY":
            random.randint(
                0,
                1000
            ),

        "CREATED_DATE":
            created_date,

        "UPDATED_DATE":
            updated_date
    })


products_df = pd.DataFrame(
    products
)


products_df.to_csv(
    os.path.join(
        DATA_DIR,
        "products.csv"
    ),
    index=False
)


print(
    f"Products created: "
    f"{len(products_df)}"
)

# 5. GENERATE STORES
print()
print("Generating stores...")


cities = [

    ("Jaipur", "Rajasthan"),

    ("Delhi", "Delhi"),

    ("Mumbai", "Maharashtra"),

    ("Pune", "Maharashtra"),

    ("Bangalore", "Karnataka"),

    ("Chennai", "Tamil Nadu"),

    ("Ahmedabad", "Gujarat"),

    ("Kolkata", "West Bengal"),

    ("Hyderabad", "Telangana"),

    ("Lucknow", "Uttar Pradesh"),

    ("Gurgaon", "Haryana"),

    ("Kochi", "Kerala"),

    ("Indore", "Madhya Pradesh"),

    ("Bhopal", "Madhya Pradesh"),

    ("Surat", "Gujarat"),

    ("Noida", "Uttar Pradesh"),

    ("Nagpur", "Maharashtra"),

    ("Chandigarh", "Chandigarh"),

    ("Patna", "Bihar"),

    ("Coimbatore", "Tamil Nadu")
]


stores = []


for i in range(NUM_STORES):

    city, state = cities[i]

    if state in [
        "Rajasthan",
        "Delhi",
        "Haryana",
        "Uttar Pradesh",
        "Chandigarh"
    ]:
        region = "NORTH"

    elif state in [
        "Maharashtra",
        "Gujarat"
    ]:
        region = "WEST"

    elif state in [
        "Karnataka",
        "Tamil Nadu",
        "Kerala",
        "Telangana"
    ]:
        region = "SOUTH"

    else:
        region = "EAST"


    stores.append({

        "STORE_ID":
            101 + i,

        "STORE_NAME":
            f"RetailMart {city}",

        "CITY":
            city,

        "STATE":
            state,

        "COUNTRY":
            "India",

        "REGION":
            region,

        "MANAGER":
            fake.name(),

        "OPENED_DATE":
            random_date(
                datetime(2020, 1, 1),
                datetime(2025, 1, 1)
            )
    })


stores_df = pd.DataFrame(
    stores
)


stores_df.to_csv(
    os.path.join(
        DATA_DIR,
        "stores.csv"
    ),
    index=False
)


print(
    f"Stores created: "
    f"{len(stores_df)}"
)

# 6. GENERATE ORDERS
print()
print("Generating orders...")


orders = []


customer_ids = (
    customers_df["CUSTOMER_ID"]
    .tolist()
)


store_ids = (
    stores_df["STORE_ID"]
    .tolist()
)


order_statuses = [
    "COMPLETED",
    "COMPLETED",
    "COMPLETED",
    "PENDING",
    "CANCELLED",
    "RETURNED"
]


payment_statuses = [
    "PAID",
    "PAID",
    "PAID",
    "PENDING",
    "FAILED",
    "REFUNDED"
]


for order_id in range(
    1000001,
    1000001 + NUM_ORDERS
):

    order_date = random_date(
        START_DATE,
        END_DATE
    )

    orders.append({

        "ORDER_ID":
            order_id,

        "CUSTOMER_ID":
            random.choice(
                customer_ids
            ),

        "STORE_ID":
            random.choice(
                store_ids
            ),

        "ORDER_DATE":
            order_date,

        "ORDER_STATUS":
            random.choice(
                order_statuses
            ),

        "PAYMENT_STATUS":
            random.choice(
                payment_statuses
            ),

        "TOTAL_AMOUNT":
            0,

        "UPDATED_DATE":
            order_date +
            timedelta(
                minutes=random.randint(
                    1,
                    1440
                )
            )
    })


orders_df = pd.DataFrame(
    orders
)

# 7. GENERATE ORDER ITEMS
print()
print("Generating order items...")


order_items = []

order_item_id = 1


product_lookup = (
    products_df
    .set_index("PRODUCT_ID")
    ["PRICE"]
    .to_dict()
)


product_ids = (
    products_df["PRODUCT_ID"]
    .tolist()
)


for _, order in orders_df.iterrows():

    number_of_items = random.randint(
        1,
        5
    )

    selected_products = random.sample(
        product_ids,
        number_of_items
    )

    order_total = 0


    for product_id in selected_products:

        quantity = random.randint(
            1,
            5
        )

        unit_price = (
            product_lookup[product_id]
        )

        discount = round(
            unit_price *
            quantity *
            random.uniform(
                0,
                0.20
            ),
            2
        )

        net_amount = (
            unit_price * quantity
        ) - discount


        order_items.append({

            "ORDER_ITEM_ID":
                order_item_id,

            "ORDER_ID":
                order["ORDER_ID"],

            "PRODUCT_ID":
                product_id,

            "QUANTITY":
                quantity,

            "UNIT_PRICE":
                unit_price,

            "DISCOUNT":
                discount
        })


        order_total += net_amount

        order_item_id += 1


    orders_df.loc[
        orders_df["ORDER_ID"]
        == order["ORDER_ID"],
        "TOTAL_AMOUNT"
    ] = round(
        order_total,
        2
    )


order_items_df = pd.DataFrame(
    order_items
)


# Save orders

orders_df.to_csv(
    os.path.join(
        DATA_DIR,
        "orders.csv"
    ),
    index=False
)


# Save order items

order_items_df.to_csv(
    os.path.join(
        DATA_DIR,
        "order_items.csv"
    ),
    index=False
)


print(
    f"Orders created: "
    f"{len(orders_df)}"
)

print(
    f"Order items created: "
    f"{len(order_items_df)}"
)

# 8. GENERATE JSON EVENTS
print()
print("Generating customer events...")


event_types = [

    "PRODUCT_VIEW",

    "ADD_TO_CART",

    "REMOVE_FROM_CART",

    "PURCHASE",

    "SEARCH"
]


events = []


# Create a quick lookup for product categories

product_category_lookup = (
    products_df
    .set_index("PRODUCT_ID")
    ["CATEGORY"]
    .to_dict()
)


for i in range(
    1,
    NUM_EVENTS + 1
):

    customer_id = random.choice(
        customer_ids
    )

    product_id = random.choice(
        product_ids
    )


    event = {

        "event_id":
            f"EVT{i:07d}",

        "customer_id":
            customer_id,

        "event_type":
            random.choice(
                event_types
            ),

        "event_timestamp":
            random_date(
                START_DATE,
                END_DATE
            ).isoformat(),

        "device": {

            "type":
                random.choice([
                    "mobile",
                    "desktop",
                    "tablet"
                ]),

            "os":
                random.choice([
                    "Android",
                    "iOS",
                    "Windows",
                    "MacOS"
                ])
        },

        "product": {

            "product_id":
                product_id,

            "category":
                product_category_lookup[
                    product_id
                ]
        }
    }


    events.append(event)


# Save JSON Lines

with open(
    os.path.join(
        DATA_DIR,
        "customer_events.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    for event in events:

        f.write(
            json.dumps(event)
            + "\n"
        )


print(
    f"Events created: "
    f"{len(events)}"
)

# 9. FINAL MESSAGE
print()
print("==========================================")
print("SOURCE DATA GENERATION COMPLETE")
print("==========================================")

print(
    f"Customers   : {len(customers_df)}"
)

print(
    f"Products    : {len(products_df)}"
)

print(
    f"Stores      : {len(stores_df)}"
)

print(
    f"Orders      : {len(orders_df)}"
)

print(
    f"Order Items : {len(order_items_df)}"
)

print(
    f"JSON Events : {len(events)}"
)

print()
print(
    f"Files created inside:"
)

print(DATA_DIR)

print("==========================================")
