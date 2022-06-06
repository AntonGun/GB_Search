# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class Book24Pipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.librarybooks

    def process_item(self, item, spider):

        if spider.name == 'book24':
            item['price'] = self.process_price(item['price'])

        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item

    def process_price(self, price):
        price = price.split(' ')[0]  # remove last sign RUB
        return price
