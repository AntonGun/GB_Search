import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from castorama.items import CastoramaItem

class CastoramaparseSpider(scrapy.Spider):
    name = 'castoramaparse'
    allowed_domains = ['castorama.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = ['https://www.castorama.ru/gardening-and-outdoor/gardening-equipment/lawn-mowers']


    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='next i-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//a[@class="product-card__name ga-product-card-name"]')
        for link in links:
            yield response.follow(link, callback=self.seeker)


    def seeker(self, response: HtmlResponse):
        '''name = response.xpath('//h1/text()').get()
        price_new = response.xpath('//div[@class="current-price"]/div/span/span/span/span/text()').get()
        price_old = response.xpath('//div[@class="old-price"]/div/span/span/span/span/text()').get()
        url = response.url
        photo = response.xpath('//li/div/img[@class="top-slide__img swiper-lazy swiper-lazy-loaded"]/@src').getall()
        yield CastoramaItem(name=name, price_new=price_new, price_old=price_old, url=url, photo=photo)'''

        loader = ItemLoader(item=CastoramaItem(), response=response)
        loader.add_xpath('name', '//h1[@class="product-essential__name hide-max-small"]/text()')
        loader.add_xpath('photo', '//li/div/img/@data-src')
        loader.add_value('url', response.url)
        loader.add_xpath('price_new', '//div[@class="current-price"]/div/span/span/span/span/text()')
        loader.add_xpath('price_old', '//div[@class="old-price"]/div/span/span/span/span/text()')
        yield loader.load_item()

