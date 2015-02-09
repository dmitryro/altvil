# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import template
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from models import GeoData

register = template.Library()

# General purpose contact form
class GeoForm(NgFormValidationMixin, NgModelFormMixin, ModelForm):
    form_name = 'geo_form'

    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='')
        super(GeoForm, self).__init__(*args, **kwargs)
        self.fields['site'].widget.attrs.update({'class' : 'search-panel-field'})
        self.fields['threshold'].widget.attrs.update({'class' : 'search-panel-field'})

    class Meta:
        model = GeoData
        fields = ['site','threshold']


        def __init__(self, *args, **kwargs):

            super(GeoForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(MemberLoginForm, self).clean()
        threshold = cleaned_data.get("threshold")
        site = cleaned_data.get("site")
