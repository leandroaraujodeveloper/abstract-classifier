# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item
from scrapy import Field

class ArxivCrawlerItem(Item):
    pass

class Publish(Item):
    title = Field()
    abstract = Field()
    field = Field()
    search_word = Field()
