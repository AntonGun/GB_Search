# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def price_processor(value):
    if value:
        try:
            value = int(value)
        except:
            return value
        return value

class CastoramaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    photo = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
    price_new = scrapy.Field(input_processor=MapCompose(price_processor), output_processor=TakeFirst())
    price_old = scrapy.Field(input_processor=MapCompose(price_processor), output_processor=TakeFirst())
    _id = scrapy.Field()

