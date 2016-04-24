# -*- coding: utf-8 -*-
import scrapy
from community_datasets.middlewares import TwitterListMembersRequest, to_item


class ElectedOfficialsTwitterSpider(scrapy.Spider):
    name = "elected_officials_twitter"

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
            # Get original size
            member['profile_image_url'] = member['profile_image_url'].replace('_normal', '')
            item = to_item(member)
            if 'url' in item:
                # Resolve the website url from the Twitter shortlink
                request = scrapy.Request(item['url'], callback=self.resolve_redirect)
                request.meta['dont_obey_robotstxt'] = True
                request.meta['item'] = item

                yield request
            else:
                yield item

    def resolve_redirect(self, response):
        item = response.meta['item']
        item['url'] = response.url
        yield item
