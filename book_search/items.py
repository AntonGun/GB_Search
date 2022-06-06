# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookSearchItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    title = scrapy.Field()
    authors = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    rate = scrapy.Field()
    _id = scrapy.Field()
    pass
