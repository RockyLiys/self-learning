# coding=utf-8
from django.conf.urls import url, include, patterns
import views


urlpatterns = patterns(
    '',

    url(r'^$', views.AngularjsIndex.as_view(), name='angularjs_index'),

    )
