# coding=utf-8
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.


class CssIndex(TemplateView):
    template_name = 'css_index.html'

    def get_context_data(self, **kwargs):
        context = super(CssIndex, self).get_context_data(**kwargs)
        return context
