"""
Create by Killer at 2019-05-17 15:30
"""
import datetime

import requests
import uplink


@uplink.response_handler
def raise_for_status(response):
    response.raise_for_status()
    return response


@uplink.json
@raise_for_status
class BlogClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://consumer_services_api.talkpython.fm')

    @uplink.get('/api/blog')
    def all_entries(self) -> requests.models.Response:
        """Get't all blog entries from the server."""

    @uplink.get('/api/blog/{post_id}')
    def entry_by_id(self, post_id) -> requests.models.Response:
        """ Get single blog post details. """

    def create_new_entry(self, title:str, content:str,
                         views:int=0, published:str=None) -> requests.models.Response:
        if published is None:
            published = datetime.datetime.now().isoformat()

        # noinspection PyTypeChecker
        return self.__create_new_entry(title=title, content=content, view_count=views,published=published)

    @uplink.post('/api/blog')
    def __create_new_entry(self, **kwargs: uplink.Body) -> requests.models.Response:
        """Create a new post"""

