CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
    )
"""


INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_PRODUCT_DETAILS = """
    CREATE TABLE IF NOT EXISTS product_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    category VARCHAR(255),
    info_product TEXT)
    """


INSERT_PRODUCTS_QUERY_DETAILS = """
INSERT INTO product_details (product_id, category, info_product) VALUES (?, ?, ?)
"""