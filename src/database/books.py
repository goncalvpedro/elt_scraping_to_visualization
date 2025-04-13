from db_connection import connect_to_db


def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dim_books (
                id SERIAL PRIMARY KEY,
                search_term VARCHAR(100) NOT NULL,
                book_author VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        return {'status': 200, 'message': 'Table ready to go.'}

    except Exception as e:
        return {'status': 500, 'message': f'Unable to create table "dim_books" due an error: {e}'}

def insert_into_books(row):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO dim_books (search_term, book_author) VALUES (%s, %s)
        ''', (row.search_term, row.book_author))
        return {'status': 200, 'message': 'Data inserted successfully.'}
    except Exception as e:
        return {'status': 500, 'message': f'Unable to insert data into "dim_books" due an error: {e}'}

def read_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT * FROM dim_books;
        ''')
        books = cursor.fetchall()

        return books

    except Exception as e:
        return {'status': 500, 'message': f'Unable to read table "dim_books" due an error: {e}'}
