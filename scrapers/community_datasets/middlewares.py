import twitter
from scrapy import log
from scrapy.http import Request, Response


class TwitterListMembersRequest(Request):

    def __init__(self, *args, **kwargs):
        self.list_slug = kwargs.pop('list_slug', None)
        super(TwitterListMembersRequest, self).__init__('http://twitter.com', dont_filter=True,**kwargs)


class TwitterResponse(Response):

    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('users', None)
        super(TwitterResponse, self).__init__('http://twitter.com', *args, **kwargs)


# See: https://github.com/yall/scrapy-twitter
class TwitterDownloaderMiddleware(object):

    def __init__(self,
                 consumer_key, consumer_secret,
                 access_token_key, access_token_secret):
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=access_token_key,
                               access_token_secret=access_token_secret)
        log.msg('Using creds [CONSUMER KEY: %s, ACCESS TOKEN KEY: %s]' %
                (consumer_key, access_token_key),
                level=log.INFO)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        consumer_key = settings['TWITTER_CONSUMER_KEY']
        consumer_secret = settings['TWITTER_CONSUMER_SECRET']
        access_token_key = settings['TWITTER_ACCESS_TOKEN_KEY']
        access_token_secret = settings['TWITTER_ACCESS_TOKEN_SECRET']
        return cls(consumer_key,
                   consumer_secret,
                   access_token_key,
                   access_token_secret)

    def process_request(self, request, spider):

        if isinstance(request, TwitterListMembersRequest):
            users = self.api.GetListMembers(slug=request.list_slug.split('/')[1],
                                             list_id=None,
                                             owner_screen_name=request.list_slug.split('/')[0])

            return TwitterResponse(users=[user.AsDict() for user in users])

    def process_response(self, request, response, spider):
        return response

from scrapy.item import DictItem, Field

def to_item(dict_user):
    field_list = dict_user.keys()
    fields = {field_name: Field() for field_name in field_list}
    item_class = type('UserItem', (DictItem,), {'fields': fields})
    return item_class(dict_user)
