import scrapy
from scrapy.http import HtmlResponse
from book_search.items import BookSearchItem

class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/search/?q=%D1%81%D1%82%D0%B8%D1%85%D0%B8']

    def parse(self, response: HtmlResponse):
        page = 1
        #while True:
        while page < 3:  # 2 pages with 30 books = 60 items
            next_page_url = 'https://book24.ru/search/page-' + str(page) + '/?q=%D1%81%D1%82%D0%B8%D1%85%D0%B8'
            if next_page_url:
                yield response.follow(next_page_url, callback=self.parse)
            page += 1
        book_links = response.xpath('//div[@class="product-list catalog__product-list"]//a[@class="product-card__image-link smartLink"]/@href').getall()
        book_links_url = []  # Short link correction
        for book in book_links:
            book_links_url.append('https://book24.ru' + book)
            for book2 in book_links_url:
                yield response.follow(book2, callback=self.book_inside_lab)

    def book_inside_lab(self, response: HtmlResponse):
        book_link = response.url
        book_title = response.xpath('//h1[@class="product-detail-page__title"]/text()').get()
        book_authors = response.xpath('//ul[@class="product-characteristic__list"]/li[@class="product-characteristic__item-holder"]//a[@class="product-characteristic-link smartLink"]/text()').get()
        if book_authors is None:
            book_authors = 'Book24.ru: литература'
        book_price = response.xpath('//span[@class="app-price product-sidebar-price__price-old"]/text()').get()
        book_discount = response.xpath('//span[@class="app-price product-sidebar-price__price"]/text()').get()
        if book_price is None:
            book_price = book_discount
            book_discount = None
        book_rate = response.xpath('//span[@class="rating-widget__main-text"]/text()').get()
        yield BookSearchItem(link=book_link, title=book_title, authors=book_authors, price=book_price,
                             discount=book_discount, rate=book_rate)
        pass
        pass