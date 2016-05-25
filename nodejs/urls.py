# coding=utf-8
from django.conf.urls import url, include, patterns
import views


urlpatterns = patterns(
    '',

    url(r'^$', views.NodejsIndex.as_view(), name='nodejs_index'),

    )
