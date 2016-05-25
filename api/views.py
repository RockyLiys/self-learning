# coding:utf-8
from restful import serializers, viewsets
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.template import Context, loader, Template

import time

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def defPatterns(request):
    from api.urls import urlpatterns
    from openstack.compute.urls import urlpatterns as compute_urlpatterns
    from openstack.network.urls import urlpatterns as network_urlpatterns
    from openstack.identity.urls import urlpatterns as identity_urlpatterns
    from openstack.images.urls import urlpatterns as images_urlpatterns
    from openstack.metering.urls import urlpatterns as metering_urlpatterns
    from openstack.volume.urls import urlpatterns as volume_urlpatterns
    urls = {
        "urls": {
            "compute": list(enumerate(map(lambda x: x._regex, compute_urlpatterns))),
            "network": list(enumerate(map(lambda x: x._regex, network_urlpatterns))),
            "identity": list(enumerate(map(lambda x: x._regex, identity_urlpatterns))),
            "images": list(enumerate(map(lambda x: x._regex, images_urlpatterns))),
            "metering": list(enumerate(map(lambda x: x._regex, metering_urlpatterns))),
            "volume": list(enumerate(map(lambda x: x._regex, volume_urlpatterns))),
        }
    }
    t = loader.get_template('index.html')
    c = Context(urls)
    return HttpResponse(t.render(c))


def process(request):
    from openstack.config import configs
    uri = request.GET.get("uri")
    labels = configs.get(uri, [])
    if labels:
        parms = {
            "uri": '/xiangcloud/api/' + uri,
            "labels": labels,
            "method": labels.get("method", []),
            "timestamp": str(int(time.time() * 1000000)),
        }
        if parms.get("labels"):
            return render_to_response('right.html', parms)
    return HttpResponse("")


class IndexView(TemplateView):
    template_name = 'xiangcloud.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class InfoView(TemplateView):
    template_name = 'info.html'

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        return context


class Test(TemplateView):
    def get_context_data(self, *args, **kwargs):
        return super(Test, self).get_context_data(**kwargs)


def test_view(request, *args, **kwargs):
    ss = Test()
    print ss, type(ss), dir(ss.response_class)
    resp = ss.response_class
    import pdb
    pdb.set_trace()
    return ss.response_class