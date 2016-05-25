# coding=utf-8
from django.views.generic.base import TemplateView
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from alipay import Alipay

import random
import string
import time

class AlipayIndex(TemplateView):
    template_name = 'alipay_index.html'

    def get_context_data(self, **kwargs):
        context = super(AlipayIndex, self).get_context_data(**kwargs)
        return context

class AlipayNotifyUrl(TemplateView):

    def post(self, *args, **kwargs):
        print dict(self.request.POST.items())
        return render_to_response('alipay_dialog_top.html', {})
        # return HttpResponseRedirect(reverse(''))

class AlipayReturnUrl(TemplateView):
    template_name = 'alipay_dialog_top.html'

    def get_context_data(self, **kwargs):
        context = super(AlipayReturnUrl, self).get_context_data(**kwargs)
        print dict(self.request.GET.items())
        return context

class TransferCash(TemplateView):

    def make_time_id(self, x=6):
        _random = "".join(random.sample(string.lowercase + string.digits, x))
        _time = str(int(round(time.time() * 1000)))[2:]
        _id = _random[:3] + _time + _random[3:]
        return _id

    def post(self, request, *args, **kwargs):

        account = request.POST.get('account')
        print account
        your_alipay_pid = '2088201436263456'
        your_alipay_key = 'zrm0gapvir2dfrjmixcis2dfntxoy3ja'
        alipay = Alipay(pid=your_alipay_pid, key=your_alipay_key, seller_email='shenzhou169@gmail.com')
        print alipay
        trade_no = self.make_time_id(10)
        print trade_no
        params = dict(
            out_trade_no=trade_no,
            subject=u'象云科技',
            total_fee='%.2f' % float(account),
            return_url='http://122.115.43.61:9999/alipay/alipay_return_url',
            notify_url='http://122.115.43.61:9999/alipay/alipay_notify_url',
        )
        alipay_url = alipay.create_direct_pay_by_user_url(**params)
        print alipay_url
        # return HttpResponse(alipay_url)
        new_html = """
            <script type='text/javascript'>
                window.open('%(alipay_url)s');
            </script>
        """ % {'alipay_url': alipay_url}
        # return HttpResponse(new_html)
        return HttpResponseRedirect(alipay_url)


