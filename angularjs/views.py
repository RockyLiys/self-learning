# coding=utf-8
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.


class AngularjsIndex(TemplateView):
    template_name = 'angularjs_index.html'

    def get_context_data(self, **kwargs):
        context = super(AngularjsIndex, self).get_context_data(**kwargs)
        return context
