# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GushiwenItem(scrapy.Item):
    # define the fields for your item here like:
    atype = scrapy.Field()
    dynasty = scrapy.Field()
    xtype = scrapy.Field()

    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
