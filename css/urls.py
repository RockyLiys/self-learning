# coding=utf-8
from django.conf.urls import url, include, patterns
import views


urlpatterns = patterns(
    '',

    url(r'^$', views.CssIndex.as_view(), name='css_index'),

    )
