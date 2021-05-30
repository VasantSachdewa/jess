from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View
from scraper.controllers.website_config_controller import WebsiteConfigController
from jess.libs.logs import Logs
from scraper.exceptions.request_exceptions import BadRequestException
import json

logger = Logs.get_logger('SCRAPER')

# Create your views here.
def index(request):
    return HttpResponse("Hello World, You're at the poll index")

class WebsiteConfig(View):

    def get(self, request, *args, **kwargs):
        web_id = request.GET.get('id')
        try:
            if not web_id:
                error = 'No id was sent to request'
                raise BadRequestException(error)
            casted_id = int(web_id)
        except BadRequestException:
            return HttpResponseBadRequest(
                json.dumps({'message': 'Invalid request'}), content_type='application/json')
        except ValueError:
            logger.error("Invalid request id '{}'".format(web_id))
            return HttpResponseBadRequest(
                json.dumps({'message': 'Invalid request'}), content_type='application/json')

        controller = WebsiteConfigController()
        resp = controller.get_config(casted_id)

        return HttpResponse(json.dumps(resp), content_type='application/json') 
