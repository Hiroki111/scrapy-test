# -*- coding: utf-8 -*-
import scrapy
from time import sleep
import random


class QuotesSpider(scrapy.Spider):
    sleep(random.randrange(1, 3))
    name = 'quotes'
    allowed_domains = [
        'www.goodreads.com/author/quotes/8330589.Miyamoto_Musashi']
    start_urls = [
        'http://www.goodreads.com/author/quotes/8330589.Miyamoto_Musashi/']

    def parse(self, response):
        quote = response.xpath(
            '//*[@class="quoteText"]/text()').extract_first()
        quotes = response.xpath('//*[@class="quoteText"]/text()').extract()

        yield {'quote': quote, 'quotes': quotes}
