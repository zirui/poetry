#!/usr/bin/python
# coding:utf8

import scrapy
import sys
from scrapy.http import Request
from artbot.items import GushiwenItem
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


reload(sys)
sys.setdefaultencoding("utf-8")



class GushiwenPoetrySpider(scrapy.Spider):
    name = "gushiwen_poetry"
    allowed_domains = ["gushiwen.org"]
    """
    t = ['写景', '咏物', '春天', '夏天', '秋天',
    '冬天', '写雨', '写雪' '写风','写花',
    '梅花', '荷花', '菊花']
    """
    t = ['不限']
    c = ['先秦', '两汉', '魏晋', '南北朝', '隋代',
    '唐代', '五代', '宋代', '金朝', '元代', '明代',
    '清代']

    x = ['诗', '词', '曲', '文言文']
    pages = {
        ""
    }
    start_urls = [
        # "http://so.gushiwen.org/type.aspx?p=1&c=先秦"
        "http://so.gushiwen.org/type.aspx"
    ]

    def start_requests(self):
        base_url = self.start_urls[0]
        for ti in self.t:
            for cj in self.c:
                for xk in self.x:
                    for p in range(1, 201):
                        # url = '%s?p=%s&t=%s&c=%s&x=%s' % (base_url, p, ti, cj, xk)
                        url = '%s?p=%s&c=%s&x=%s' % (base_url, p, cj, xk)
                        info = {"atype": ti, 'dynasty': cj, 'xtype': xk}
                        # print url
                        # request = Request(url, meta=info),
                        # yield request
                        yield Request(url, callback=self.parse, meta=info)

    def parse(self, response):
        meta = response.meta
        sons = response.xpath("/html/body//div[@class='typeleft']//div[@class='sons']")
        for sel in sons:
            title = sel.xpath('p/a/text()').extract()[0]
            author = sel.xpath('p/text()').extract()[0]
            content = sel.xpath('p/text()').extract()[1]

            item = GushiwenItem()
            item['atype'] = meta['atype']
            item['dynasty'] = meta['dynasty']
            item['xtype'] = meta['xtype']

            item['title'] = title
            item['title'] = author
            item['content'] = content
            yield item
