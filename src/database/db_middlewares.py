import pandas as pd
import books

def get_books_to_scrape():
    books.create_table()
    data = pd.read_csv('books_to_scrape.csv')

    try:
        book_list = []

        for index, book_series in data.iterrows():
            row = book_series.to_dict()
            book_list.append(row)

            books.insert_into_books(row)

        return {'status': 200, 'message': 'Initial data inserted into dim_books table.'}

    except Exception as e:
        return {'status': 500, 'message': f'Unable to insert initial data into table "dim_books" due an error: {e}'}

