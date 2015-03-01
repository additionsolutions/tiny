from django import forms
from django.contrib.auth.models import User, Group
#from base.models import Category, Page, User, UserProfile

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    


    def signup(self, request, user):
        role = request.session.get('user_type')
        group = role or "Default"
        g = Group.objects.get(name=group)
        user.groups.add(g)
        user.save()