CREATE TABLE dim_books (
    id SERIAL PRIMARY KEY,
    search_term VARCHAR(100) NOT NULL,
    book_author VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);