from django.shortcuts import render
from django.http import HttpResponse
from jess.libs.logs import Logs

logger = Logs.get_logger('SCRAPER')

# Create your views here.
def index(request):
    return HttpResponse("Hello World, You're at the poll index")

def sync_website(request):
    '''
        Sync website jobs from website
    '''
    #get seller id
    #get configs
    #call controller

def  add_website_configuration(request):
    '''
        Add new website configuration 
        into datastore
    '''
    if request.method == 'GET':
        #handle GET
        #check if id is int type or castable
        #throw bad request if not castable

    if request.method == 'POST':
        #handle POST
