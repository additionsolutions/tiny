from django.shortcuts import render
from django.views import generic
from braces import views
from base.models import UserProfile

# Create your views here.

def basic(request, template_name='dmin/basic.html'):
    #contenttype = ContentType.objects.all()
    data = {}
    data['object_list'] = " " #contenttype
    return render(request, template_name, data)
    
    
class UserListView(views.LoginRequiredMixin, generic.ListView):
    model = UserProfile
    template_name = "userlist.html"
    
    def get_queryset(self):
        self.messages.success("You've been logged out. Come back soon!")
        return self.request.user.lists.all()