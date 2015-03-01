from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from allauth.account.views import LoginView, SignupView, LogoutView
from django.contrib.auth.models import User, Group

def index(request):
    context = RequestContext(request)
    context_dict = {'message': 'Hello Rahul Shinde'}
    return render_to_response('base/index.html', context_dict, context)
    
def login(request):
    # context = RequestContext(request)
    # context_dict = {'boldmessage': "Please Login"}
    # return render_to_response('allauth/base.html', context_dict, context)
    LoginView(request)
 
def signup(request):
    # context = RequestContext(request)
    # context_dict = {'boldmessage': "Please Login"}
    # return render_to_response('allauth/account/signup.html', context_dict, context)
    SignupView(request)
    
def profile(request):
    context = RequestContext(request)
    context_dict = {'message': "Welcome " }
    link = 'base/index.html'
    for g in request.user.groups.all():
        if g.name == 'site_admin':
            link = 'allauth/account/profile.html'
    return render_to_response(link, context_dict, context)
    
def logout(request):
    # context = RequestContext(request)
    # context_dict = {'boldmessage': "Please Login"}
    # return render_to_response('allauth/base.html', context_dict, context)
    LogoutView(request)