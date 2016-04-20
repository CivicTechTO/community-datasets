# -*- coding: utf-8 -*-
import scrapy


class ElectedOfficialsTwitterSpider(scrapy.Spider):
    name = "elected_officials_twitter"
    allowed_domains = ["twitter.com"]
    start_urls = (
        'http://www.twitter.com/',
    )

    def parse(self, response):
        pass
