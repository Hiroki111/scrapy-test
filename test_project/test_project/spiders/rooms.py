# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy import Request
from scrapy.loader import ItemLoader
from test_project.items import PriceSpiderItem
from time import sleep
import random


class RoomsSpider(Spider):
    sleep(random.randrange(1, 3))
    name = 'rooms'
    allowed_domains = ['flatmates.com.au']
    start_urls = [
        'http://flatmates.com.au/rooms/annerley-4103/males']

    def parse(self, response):
        rooms = response.xpath(
            './/*[@class="ribbon property"]/text()')
        item = PriceSpiderItem()
        item['prices'] = rooms.extract()
        yield item

        nextUrl = response.xpath(
            '//*[@aria-label="Go to next page"]/@href').extract_first()

        if(nextUrl is not None):
            absoluteNextUrl = response.urljoin(nextUrl)
            yield Request(url=absoluteNextUrl, callback=self.parse)
