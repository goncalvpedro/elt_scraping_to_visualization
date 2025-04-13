from pathlib import Path
from datetime import datetime as dt

# Current timestamp formatted
NOW = dt.now().strftime("%Y-%m-%d_%H-%M-%S")

# Base project path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
# C:\Projetos\data-engineering\elt-scrapy\

CSV_URL = PROJECT_ROOT / 'books_to_scrape.csv'

SCRAPE_FOLDER = PROJECT_ROOT / 'src' / 'scraping'
DATABASE_FOLDER = PROJECT_ROOT / 'src' / 'database'
TRANSFORM_FOLDER = PROJECT_ROOT / 'src' / 'transform'

# HTML elements
BOOK_DIV_XPATH = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div'
BOOK_NAME_XPATH = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[3]/div[1]/a/h2'
BOOK_AUTHOR_XPATH = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[3]/div[1]/div/span[2]'
BOOK_RATING_XPATH = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[3]/div[1]/div/span[2]'
BOOK_RATING_AMOUNT_XPATH = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[3]/div[2]/div/a/span'
BOOK_FORMAT_XPATH = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[3]/div[3]/div[1]/a'
BOOK_PRICE_XPATH = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div[3]/div[3]/div[2]/div[1]/a/span[1]/span[2]'

# OUTPUT FILE
OUTPUT_FILE = PROJECT_ROOT
