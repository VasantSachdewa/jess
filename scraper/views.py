import json

from django.http import HttpResponse, HttpResponseBadRequest
from jess.libs.logs import Logs
from rest_framework.views import APIView

from scraper.controllers.website_config_controller import \
    WebsiteConfigController
from scraper.exceptions.request_exceptions import BadRequestException
from scraper.validators import WebsiteConfigPostValidator, WebsiteConfigPutValidator

logger = Logs.get_logger('SCRAPER')

# Create your views here.
def index(request):
    return HttpResponse("Hello World, You're at the poll index")

class WebsiteConfig(APIView):
    
    post_request_validator = WebsiteConfigPostValidator
    put_request_validator = WebsiteConfigPutValidator

    def __init__(self):
        self.controller = WebsiteConfigController()

    def get(self, request):
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

        resp = self.controller.get_config(casted_id)

        return HttpResponse(json.dumps(resp), content_type='application/json') 

    def post(self, request):
        #validate request using validator
        request_body = self.post_request_validator(data=request.data)
        try:
            if not request_body.is_valid():
                #handle error
                error = 'Invalid request body {}'.format(request.data)
                raise BadRequestException(error)
        except BadRequestException:
            logger.error('Invalid request body {}'.format(request.data))
            return HttpResponseBadRequest(
                json.dumps({'message': 'Invalid request'}), content_type='application/json')

        #handle success
        resp = self.controller.add_config(request.data)
        #return response
        return HttpResponse(json.dumps(resp), content_type='application/json') 

    def put(self, request):
        request_body = self.put_request_validator(data=request.data)
        try:
            if not request_body.is_valid():
                error = 'Invalid request body {}'.format(request.data)
                raise BadRequestException(error)
        except BadRequestException:
            logger.error('Invalid request body {}'.format(request.data))
            return HttpResponseBadRequest(
                json.dumps({'message': 'Invalid request'}), content_type='application/json')

        resp = self.controller.update_config(request.data)
        return HttpResponse(json.dumps(resp), content_type='application/json') 

