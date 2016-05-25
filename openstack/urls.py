from __future__ import unicode_literals
from django.conf.urls import url, include, patterns
from django.views.generic import RedirectView

import views

# import cloudformation.views  as cloudformation_views
# import compute.views as compute_views
# import identity.views as identity_views
# import images.views as images_views
# import metering.views as metering_views
# import network.views as network_views
# import orchestration.views as orchestration_views
# import volume.views as volume_views
# import volumev2.views as volumev2_views

from compute.urls import urlpatterns as compute_urlpatterns
from network.urls import urlpatterns as network_urlpatterns
from identity.urls import urlpatterns as identity_urlpatterns
from volume.urls import urlpatterns as volume_urlpatterns
from images.urls import urlpatterns as images_urlpatterns
from metering.urls import urlpatterns as metering_urlpatterns

urlpatterns = compute_urlpatterns + network_urlpatterns + identity_urlpatterns + volume_urlpatterns + images_urlpatterns + metering_urlpatterns


urlpatterns += patterns(
    'openstack',

    # url(r'^$', RedirectView.as_view(url='/obtainToken/')),
    url(r'test/', views.test),
    url(r'options', views.options_test),
    url(r'head', views.head_test),
    url(r'put', views.put_test),
    url(r'post', views.post_test),
    url(r'patch', views.patch_test),



    # url(r'^addUser/',views.addUser,name='add'),
    url(r'obtainUser/', views.obtaindetailUserByName, name='obtain'),

    # Bare metal

    # cloud host

    # images

    # cloud hareware

    # snapshot

    # route

    # network

    # security

    # ssh_keys

    # load blance

    # vpn

    # public ip

    # db service

    # pos recodes

    # select recodes

    # monitor

)
