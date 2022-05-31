from lxml import html
import requests
from pprint import pprint

#DataBase
import pymongo
client = MongoClient('localhost', 27017)
data_base = client['News_DB']
collection = data_base['Ya_Mail']

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"}
url_mail = 'https://news.mail.ru/'

response = requests.get(url_mail, headers=headers)
dom = html.fromstring(response.text)
news_mail = dom.xpath("//li[contains(@class,'list__item')]")

news_list = []

for new in news_mail:
    news_dict = {}

    name = new.xpath('.//span[@class = "link__text"]/text() | .//a[@class = "list__text"]/text()')
    link = new.xpath('.//span[@class = "link__text"]/../@href | .//a[@class = "list__text"]/@href')
    date = None
    source = url_mail[8:].partition('/')[0]

    news_dict['Title'] = name
    news_dict['Link'] = link
    news_dict['Date'] = date
    news_dict['Source'] = source

    news_list.append(news_dict)
    # Insert to DB
    ins = collection.insert_one(news_dict)

url_yandex = 'https://yandex.ru/news/'

response_y = requests.get(url_yandex, headers=headers)
dom_y = html.fromstring(response_y.text)
news_y = dom_y.xpath('//h2[contains(@class, "mg-card")]')

for new in news_y:
    news_dict = {}

    name = new.xpath('.//a[@class = "mg-card__link"]/text()')
    link = new.xpath('.//a[@class = "mg-card__link"]/@href')
    date = new.xpath('.//span[@class = "mg-card-source__time"]/text()')
    source = url_yandex[8:].partition('/')[0]

    news_dict['Title'] = name
    news_dict['Link'] = link
    news_dict['Date'] = date
    news_dict['Source'] = source

    news_list.append(news_dict)
    # Insert to DB
    ins = collection.insert_one(news_dict)

pprint(news_list)



