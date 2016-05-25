# coding=utf-8
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.


class BootstrapIndex(TemplateView):
    template_name = 'bootstrap_index.html'

    def get_context_data(self, **kwargs):
        context = super(BootstrapIndex, self).get_context_data(**kwargs)
        return context
