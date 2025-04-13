import scrapy


class BookScraperSpider(scrapy.Spider):
    name = "book_scraper"
    allowed_domains = ["amazon.com.br"]
    start_urls = ["https://amazon.com.br"]

    def parse(self, response):
        pass
