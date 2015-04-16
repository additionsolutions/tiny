from django.shortcuts import render, redirect, get_object_or_404, RequestContext, render_to_response
from django.forms import ModelForm, ModelChoiceField, HiddenInput
from contents.models import User, Content, ContentType
from django.http import HttpResponse, HttpResponseRedirect

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
        
                  
    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)
        # access object through self.instance...
        self.fields['contenttype'].queryset = ContentType.objects.exclude(name='None')

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
    if request.method == 'GET':
        notices = Content.objects.filter(groups=request.user.groups.all())
        
    return render_to_response('contents/notice.html', {'notices': notices }, context)

    