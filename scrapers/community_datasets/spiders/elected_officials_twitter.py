# -*- coding: utf-8 -*-
import scrapy
from community_datasets.middlewares import TwitterListMembersRequest, to_item


class ElectedOfficialsTwitterSpider(scrapy.Spider):
    name = "elected_officials_twitter"
    allowed_domains = ["twitter.com"]

    def __init__(self, list_slug = None, *args, **kwargs):
        if not list_slug:
            raise scrapy.exceptions.CloseSpider('Argument list_slug not set.')
        super(ElectedOfficialsTwitterSpider, self).__init__(*args, **kwargs)
        self.list_slug = list_slug

    def start_requests(self):
        return [TwitterListMembersRequest(list_slug=self.list_slug)]

    def parse(self, response):
        members = response.users

        for member in members:
            yield to_item(member)
