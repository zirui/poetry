# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs


class ArtbotPipeline(object):
    def __init__(self):
        self.rst_file_name = 'data/gushiwen_poetry.json'
        self.rst_file = codecs.open(self.rst_file_name, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.rst_file.write(line.decode('unicode_escape'))
        return item
