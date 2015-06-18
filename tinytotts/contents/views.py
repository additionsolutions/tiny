from django.shortcuts import render, redirect, get_object_or_404, RequestContext, render_to_response
from django.forms import ModelForm, ModelChoiceField, HiddenInput
from contents.models import User, Content, ContentType
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

######################################
# Content Type
######################################

class ContentTypeForm(ModelForm):

    class Meta:
        model = ContentType
        fields = ('name',
          'description')

def contenttype_list(request, template_name='contents/contenttype_list.html'):
    contenttype = ContentType.objects.all()
    data = {}
    data['object_list'] = contenttype
    return render(request, template_name, data)

def contenttype_create(request, template_name='contents/contenttype_form.html'):
    form = ContentTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contenttype_list')
    return render(request, template_name, {'form':form})


def contenttype_update(request, pk, template_name='contents/contenttype_form.html'):
    contenttype = get_object_or_404(ContentType, pk=pk)
    form = ContentTypeForm(request.POST or None, instance=contenttype)
    if form.is_valid():
        form.save()
        return redirect('contenttype_list')
    return render(request, template_name, {'form':form})


def contenttype_delete(request, pk, template_name='contents/contenttype_confirm_delete.html'):
    contenttype = get_object_or_404(ContentType, pk=pk)
    if request.method=='POST':
        contenttype.delete()
        return redirect('contenttype_list')
    return render(request, template_name, {'object':contenttype})


######################################
# Content
######################################

class ContentForm(ModelForm):

    class Meta:
        model = Content
	exclude = ('video',)
        
                  
    #def __init__(self, *args, **kwargs):
     #   super(ContentForm, self).__init__(*args, **kwargs)
        # access object through self.instance...
      #  self.fields['contenttype'].queryset = ContentType.objects.exclude(name='None')

def content_list(request, template_name='contents/content_list.html'):
    content = Content.objects.all()
    data = {}
    data['object_list'] = content
    return render(request, template_name, data)

def content_create(request, template_name='contents/content_form.html'):
    form = ContentForm(request.POST or None, initial={'createdby': request.user})
    form.fields['createdby'] = ModelChoiceField(label="", widget=HiddenInput(attrs={'value':request.user}), queryset=User.objects.all())
    if form.is_valid():
        form.save()
        return redirect('content_list')
    return render(request, template_name, {'form':form})


def content_update(request, pk, template_name='contents/content_form.html'):
    content = get_object_or_404(Content, pk=pk)
    form = ContentForm(request.POST or None, instance=content)
    if form.is_valid():
        form.save()
        return redirect('content_list')
    return render(request, template_name, {'form':form})


def content_delete(request, pk, template_name='contents/content_confirm_delete.html'):
    content = get_object_or_404(Content, pk=pk)
    if request.method=='POST':
        content.delete()
        return redirect('content_list')
    return render(request, template_name, {'object':content})


######################################
# Content Notice
######################################

def notice(request):
    context = RequestContext(request)
    notices = []
    current_date = date.today()
    if request.method == 'GET':
        notices = Content.objects.filter(contenttype=ContentType.objects.filter(name='Notice'), groups=request.user.groups.all(),startdate__lte=current_date,enddate__gte=current_date)
        
    return render_to_response('contents/notice.html', {'notices': notices }, context)

######################################
# Content Activities
######################################

def activities(request):
    context = RequestContext(request)
    activities = []
    current_date = date.today()
    if request.method == 'GET':
        activities = Content.objects.filter(contenttype=ContentType.objects.filter(name='Activities'), groups=request.user.groups.all(),startdate__lte=current_date,enddate__gte=current_date)
        
    return render_to_response('contents/activities.html', {'activities': activities }, context)
    
    
######################################
# Content Portion
######################################

def portion(request):
    context = RequestContext(request)
    portion = []
    current_date = date.today()
    if request.method == 'GET':
        portion = Content.objects.filter(contenttype=ContentType.objects.filter(name='Portion'),groups=request.user.groups.all(),startdate__lte=current_date,enddate__gte=current_date)
        
    return render_to_response('contents/portion.html', {'portion': portion }, context)