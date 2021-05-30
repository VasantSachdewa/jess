from typing import Dict, TypedDict, Any, Union
from scraper.models import Websites


class WebsiteConfigType(TypedDict):
    id: int
    name: str
    url: str


class WebsiteConfigController():
    '''
        The responsible of module is to add/delete/update
        new website configuration into datastore
    '''

    def __init__(self):
        pass

    def get_config(self, _id: int) -> Union[WebsiteConfigType, Dict]:
        website_query_set = Websites.objects.filter(id=_id)
        if website_query_set.exists():
            website_config = website_query_set.first()
            return website_config.to_dict()
        else:
            return {'message': 'id {} do not exists'.format(_id)}
