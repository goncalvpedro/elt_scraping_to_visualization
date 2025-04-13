# In construction ...

1.  Database
    - Create connectiom: Done **src/database/db_connection.py**
    - Create local database: Completed on pgAdmin 4
    - Create tables
        - dim_products
        - fact_products
    - Create relations

1.1 Products middleware
    - Get products to be scraped
    - Get them ready to scrape

2.  Scraper
    - Receive products list and iterate over it
    - Get product name, author and price
    - Return a lis of objects

2.1 Scraper middleware
    - Get list of product objects
    - Inserts into fact_prices

