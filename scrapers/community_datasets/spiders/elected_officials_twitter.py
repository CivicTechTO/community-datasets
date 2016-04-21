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
            if 'url' in member:
                member['url'] = self.resolve_redirect(member['url'])
            yield to_item(member)

    def resolve_redirect(self, url):
        # TODO: Figure out how to resolve short urls
        return url
