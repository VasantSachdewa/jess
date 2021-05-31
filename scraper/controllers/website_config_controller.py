from typing import Dict, TypedDict, Any, Union
from scraper.models import Websites
from jess.libs.logs import Logs

logger = Logs.get_logger('Scraper')


class WebsiteConfigType(TypedDict):
    id: int
    name: str
    url: str


class WebsiteConfigController():
    '''
        The responsible of module is to add/delete/update
        new website configuration into datastore

        TO-DO: 
            - Remove dependency between model library and
            controller class, perhaps use Interface and factory
            method to eliminate the dependency 
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

    def add_config(self, config: Dict) -> Union[WebsiteConfigType, Dict]:
        #create config
        try:
            website_config = Websites.objects.create(**config)
            website_config.save()
        except Exception as error:
            logger.error('Failed to create with error {}'.format(error))
            return {'message': 'Error creating config'}
        
        return website_config.to_dict()

