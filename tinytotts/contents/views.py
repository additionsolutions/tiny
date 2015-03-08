#from contents.forms import ContentTypeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from contents.models import Content, ContentType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button
from crispy_forms.bootstrap import (PrependedText,  PrependedAppendedText, FormActions, StrictButton)


class ContentTypeForm(ModelForm):
    class Meta:
        model = ContentType

def contenttype_list(request, template_name='contents/contenttype_list.html'):
    contenttype = ContentType.objects.all()
    data = {}
    data['object_list'] = contenttype
    return render(request, template_name, data)

def contenttype_create(request, template_name='contents/contenttype_form.html'):
    form = ContentTypeForm(request.POST or None)
    form.helper = FormHelper()
    form.helper.form_method = 'POST'
    form.helper.form_class = 'form-horizontal'
    form.helper.label_class = 'col-sm-2'
    form.helper.field_class = 'col-sm-6'
    form.helper.layout = Layout(
        Field('name', css_class='input-sm'),
        Field('description', css_class='input-sm'),
        FormActions(Submit('contenttype_list', 'Submit', css_class='btn btn-info'))
    )

    if form.is_valid():
        form.save()
        return redirect('contenttype_list')
    return render(request, template_name, {'form':form})


def contenttype_update(request, pk, template_name='contents/contenttype_form.html'):
    contenttype = get_object_or_404(ContentType, pk=pk)
    form = ContentTypeForm(request.POST or None, instance=contenttype)
    form.helper = FormHelper()
    form.helper.form_method = 'POST'
    form.helper.form_class = 'form-horizontal'
    form.helper.label_class = 'col-sm-2'
    form.helper.field_class = 'col-sm-6'
    form.helper.layout = Layout(
        Field('name', css_class='input-sm'),
        Field('description', css_class='input-sm'),
        FormActions(Submit('contenttype_list', 'Submit', css_class='btn btn-info'))
    )

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

