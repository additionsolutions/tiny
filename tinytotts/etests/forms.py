from django import forms
from .models import TestSet, TestSetLine
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

class TestSetForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = True
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-4'
    helper.field_class = 'col-sm-8'
    helper.layout = Layout(
        Field('code', ),
        Field('testname', css_class='input-sm'),
        Field('description', css_class='input-sm'),
        Field('startdate', css_class='input-sm'),
        Field('enddate', css_class='datepicker'),
        FormActions(Submit('/base/registration', 'Add User', css_class='btn-primary'))
    )

    class Meta:
        model = TestSet
    
    

class TestSetLineForm(forms.ModelForm):
    class Meta:
        model = TestSetLine
        exclude = ('testset',)