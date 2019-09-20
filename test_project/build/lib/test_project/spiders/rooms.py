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

    allowed_domains = [
        'flatmates.com.au/rooms/annerley-4103/males+min-150+max-180']
    start_urls = [
        'http://flatmates.com.au/rooms/annerley-4103/males+min-150+max-180/']

    def parse(self, response):
        # l = ItemLoader(item=PriceSpiderItem(), response=response)
        # for room in response.xpath('.//*[@class="ribbon property"]/text()'):
        #     price = room.extract()
        #     l.add_value('price', price)

        # yield l.load_item()
        # nextUrl = response.xpath(
        #     '/html/body/div[2]/div[2]/div/nav/div[2]/a/@href').extract_first()
        # if nextUrl is not None:
        #     absoluteNextUrl = response.urljoin(nextUrl)
        #     yield Spider.scrapy.Request(absoluteNextUrl, callback=self.parse)

        rooms = response.xpath(
            './/*[@class="ribbon property"]/text()')
        l = ItemLoader(item=PriceSpiderItem(), response=response)
        for room in rooms:
            price = room.extract()
            l.add_value('price', price)
            # print(price)

        yield l.load_item()

        nextUrl = response.xpath(
            '/html/body/div[2]/div[2]/div/nav/div[2]/a/@href').extract_first()

        absoluteNextUrl = response.urljoin(nextUrl)
        print('absoluteNextUrl ' + absoluteNextUrl)
        yield Request(url=absoluteNextUrl, callback=self.parse)
