# coding=utf-8
from django.conf.urls import url, include, patterns
from alipay import views


urlpatterns = patterns(
    'alipay',

    url(r'^$', views.AlipayIndex.as_view(), name='alipay_index'),
    url(r'/transfer_cash$', views.TransferCash.as_view(), name='transfer_cash'),

    url(r'/alipay_notify_url$', views.AlipayNotifyUrl.as_view(), name='notify_url'),
    url(r'/alipay_return_url$', views.AlipayReturnUrl.as_view(), name='return_url'),


    )
