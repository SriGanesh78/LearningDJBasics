from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import datetime

# Create your views here.
def hello_world(request):
    now = datetime.datetime.now()
    # html = "<html><body>You are hitting the Hellow World</body></html>"
    # return HttpResponse(html)

    # html = """<html>
    # <body>
    # <h1>Hello world</h1>
    # you are hitting the hello world view ! 
    # </body>
    # </html>
    # """ 
    # return HttpResponse(html)
    
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)