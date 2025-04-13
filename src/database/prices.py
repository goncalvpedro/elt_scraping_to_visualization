from db_connection import connect_to_db


def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fact_prices (
                id SERIAL PRIMARY KEY NOT NULL,
                book_id INT REFERENCES dim_books(id),
                name VARCHAR(100) NOT NULL,
                price INT NOT NULL,
                author VARCHAR(50),
                language VARCHAR(50),
                format VARCHAR(50),
                rating VARCHAR(50),
                rating_amount VARCHAR(50),
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        return {'status': 200, 'message': 'Table "fact_prices" ready to go.'}

    except Exception as e:
        return {'status': 500, 'message': f'Unable to create table due an error: {e}'}


def inserts_into_table(row):
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO fact_prices (book_id, name, price, author, language, format, rating, rating_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (row.book_id, row.name, row.price, row.author, row.language, row.format, row.rating, row.rating_amount))
        conn.commit()
        cursor.close()
        conn.close()
        return {'status': 200, 'message': f'Row added successfully into fact_prices database.'}

    except Exception as e:
        return {'status': 500, 'message': f'Unable to insert data into fact_prices table due an error: {e}'}


def read_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT * FROM fact_prices;
        ''')
        books = cursor.fetchall()

        return books

    except Exception as e:
        return {'status': 500, 'message': f'Unable to read table "fact_prices" due an error: {e}'}
