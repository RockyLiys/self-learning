# coding=utf-8
from django.conf.urls import url, include, patterns
import views


urlpatterns = patterns(
    '',

    url(r'^$', views.BootstrapIndex.as_view(), name='bootstrap_index'),

    )
