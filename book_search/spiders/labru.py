import scrapy
from scrapy.http import HtmlResponse
from book_search.items import BookSearchItem


class LabruSpider(scrapy.Spider):
    name = 'labru'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D1%81%D1%82%D0%B8%D1%85%D0%B8/?stype=0']

    def parse(self, response: HtmlResponse):
        page = 1
        #while True:
        while page < 3: #2 pages with 60 books = 120 items
            next_page_url = 'https://www.labirint.ru/search/%D1%81%D1%82%D0%B8%D1%85%D0%B8/?stype=0&page=' + str(page)
            if next_page_url:
                yield response.follow(next_page_url, callback=self.parse)
            page += 1
        book_links = response.xpath('//a[@class="product-title-link"]/@href').getall()
        book_links_url = [] #Short link correction
        for book in book_links:
            book_links_url.append('https://www.labirint.ru' + book)
            for book2 in book_links_url:
                yield response.follow(book2, callback=self.book_inside_lab)

    def book_inside_lab(self, response: HtmlResponse):
        book_link = response.url
        book_title = response.css('h1::text').get()
        book_authors = response.xpath('//div[@class="product-description"]/div[contains(text(), "Автор")]/a[@class="analytics-click-js"]/text()').get()
        if book_authors is None:
            book_authors = 'Лабиринт: Детская художественная литература'
        book_price = response.xpath('//span[@class="buying-priceold-val-number"]/text()').get()
        book_discount = response.xpath('//span[@class="buying-pricenew-val-number"]/text()').get()
        book_rate = response.xpath('//div[@id="rate"]/text()').get()
        yield BookSearchItem(link=book_link, title=book_title, authors=book_authors, price=book_price, discount=book_discount, rate=book_rate)
        pass
        pass