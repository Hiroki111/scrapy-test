# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GreenslopesSpider(CrawlSpider):
    name = "greenslopes"
    allowed_domains = ["flatmates.com.au/rooms/greenslopes-4120/males+private-room"]
    start_urls = ["http://flatmates.com.au/rooms/greenslopes-4120/males+private-room"]

    rules = (
        Rule(
            LinkExtractor(deny_domains=("twitter.com")),
            callback="parse_page",
            follow=True,
        ),
    )

    def parse_page(self, response):
        pass
