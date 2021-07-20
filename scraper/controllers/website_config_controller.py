from typing import Dict, TypedDict, Union
from scraper.models import Websites
from jess.libs.logs import Logs

logger = Logs.get_logger("Scraper")


class WebsiteConfigType(TypedDict):
    id: int
    name: str
    url: str


class WebsiteConfigController:
    """
    The responsible of module is to add/delete/update
    new website configuration into datastore

    TO-DO:
        - Remove dependency between model library and
        controller class, perhaps use adapters to eliminate the dependency
    """

    def __init__(self):
        pass

    def get_config(self, _id: int) -> Union[WebsiteConfigType, Dict]:
        website_query_set = Websites.objects.filter(id=_id)
        if website_query_set.exists():
            website_config = website_query_set.first()
            return website_config.to_dict()
        else:
            return {"message": "id {} do not exists".format(_id)}

    def add_config(self, config: Dict) -> Union[WebsiteConfigType, Dict]:
        # create config
        try:
            website_config = Websites.objects.create(**config)
            website_config.save()
        except Exception as error:
            logger.error("Failed to create with error {}".format(error))
            return {"message": "Error creating config"}

        return website_config.to_dict()

    def update_config(self, config: Dict) -> Union[WebsiteConfigType, Dict]:
        # Update flow
        if "id" in config.keys():
            try:
                website_config = Websites.objects.get(id=config["id"])
            except Exception as e:
                logger.error("Invalid query with error {}".format(e))
                return {"message": "Invalid request"}
            website_config.name = config.get("name", website_config.name)
            website_config.url = config.get("url", website_config.url)
            website_config.save()
            return website_config.to_dict()
        # Create new flow
        else:
            return self.add_config(config)

    def delete_config(self, _id: int) -> Union[WebsiteConfigType, Dict]:
        website_query_set = Websites.objects.filter(id=_id)
        if website_query_set.exists():
            website_config = website_query_set.first()
            return website_config.to_dict()
        else:
            return {"message": "id {} do not exists".format(_id)}
