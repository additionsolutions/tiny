from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User, Group

def index(request):
    context = RequestContext(request)
    context_dict = {'message': 'Hello Rahul Shinde'}
    return render_to_response('base/index.html', context_dict, context)
    
def aboutus(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "This page is about us"}
    return render_to_response('base/aboutus.html', context_dict, context)