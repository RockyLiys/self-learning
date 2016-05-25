# coding:utf-8
from restful import routers
from django.conf.urls import url, include, patterns
from django.views.generic import RedirectView
from views import UserViewSet

import views

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sss', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns(
    '',

    url(r'^admin$', include(router.urls)),

    # url(r'^$', RedirectView.as_view(url='api-auth/login/')),
    url(r'^$', views.IndexView.as_view()),
    url(r'^api-auth/', include('restful.urls', namespace='rest_framework')),
    url(r'^xiangcloud/api/', include('openstack.urls')),
    url(r'xcloud-public-api/', include('public.urls', namespace='api_public')),
    url(r'^alipay', include('alipay.urls', namespace='api_alipay')),
    url(r'^angularjs', include('angularjs.urls', namespace='api_angularjs')),
    url(r'^css', include('css.urls', namespace='api_css')),
    url(r'^nodejs', include('nodejs.urls', namespace='api_nodejs')),
    url(r'^bootstrap', include('bootstrap.urls', namespace='api_bootstrap')),


    url(r'^accounts/profile/', RedirectView.as_view(url='/xcloud-public-api/db/')),  # redirect
    url(r'^urlpatterns$', views.defPatterns),
    url(r'process/', views.process),
    url(r'^info$', views.InfoView.as_view(), name='info'),

    # test
    url(r'^test', views.test_view),

    # enter gettoken

)
