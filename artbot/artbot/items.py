# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtbotItem(scrapy.Item):
    # define the fields for your item here like:
    pass


class GushiwenItem(scrapy.Item):
    # define the fields for your item here like:
    dynasty = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    poetry = scrapy.Field()
