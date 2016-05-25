from __future__ import unicode_literals
from django.conf.urls import url, include,patterns
import views
import openstack

urlpatterns = patterns('public',


    url(r'db/',views.db_process),
    


)