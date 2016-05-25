#!/usr/bin/python
#--coding:utf-8--#

import pycurl
import urllib
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

class WebSev(object):
    
    def __init__(self):
        self.curl = pycurl.Curl()
        self.buf = BytesIO()
        
    @property
    def init_setopt(self):
        self.curl.setopt(pycurl.CONNECTTIMEOUT, 5)      # 连接等待时间，0则不等待
        self.curl.setopt(pycurl.TIMEOUT, 5)     # 超时时间
        self.curl.setopt(pycurl.DNS_CACHE_TIMEOUT, 60)      # 设置DNS信息保存时间，默认为120秒


    def url(self, url):
        return urllib.unquote(url)

    def req_headers(self):
        pass
        
    def body(self, body):
        # body type json
        return urlencode(body)
        
    def res_headers(self, headers):
        return headers
        
    def monitor(self):
        self.curl.perform()
        print "返回HTTP状态码:%s" % self.curl.getinfo(pycurl.HTTP_CODE)           # 返回HTTP状态码
        print "传输结束时所消耗的总时间:%s" % self.curl.getinfo(pycurl.TOTAL_TIME)          # 传输结束时所消耗的总时间
        print "DNS解析所消耗的时间:%s" % self.curl.getinfo(pycurl.NAMELOOKUP_TIME)     # DNS解析所消耗的时间
        print "建立连接所消耗的时间:%s" % self.curl.getinfo(pycurl.CONNECT_TIME)        # 建立连接所消耗的时间
        print "从建立连接到准备传输所消耗的时间:%s" % self.curl.getinfo(pycurl.PRETRANSFER_TIME)    # 从建立连接到准备传输所消耗的时间
        print "从建立连接到数据开始传输所消耗的时间: %s" % self.curl.getinfo(pycurl.STARTTRANSFER_TIME)  # 从建立连接到数据开始传输所消耗的时间
        print "重定向所消耗的时间:%s" % self.curl.getinfo(pycurl.REDIRECT_TIME)       # 重定向所消耗的时间
        print "上传数据包大小:%s" % self.curl.getinfo(pycurl.SIZE_UPLOAD)         # 上传数据包大小
        print "下载数据包大小:%s" % self.curl.getinfo(pycurl.SIZE_DOWNLOAD)       # 下载数据包大小
        print "平均下载速度:%s" % self.curl.getinfo(pycurl.SPEED_DOWNLOAD)      # 平均下载速度
        print "平均下载速度:%s" % self.curl.getinfo(pycurl.SPEED_UPLOAD)        # 平均上传速度
        print "HTTP头部大小:%s" % self.curl.getinfo(pycurl.HEADER_SIZE)         # HTTP头部大小
        
    def get_data(self, url):
        self.init_setopt
        self.curl.setopt(pycurl.URL, self.url(url))     # 设置url
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf.write)
        self.monitor()

    def post_data(self, url, body):
        self.init_setopt
        self.curl.setopt(pycurl.URL, self.url(url))     # 设置url
        self.curl.setopt(pycurl.POSTFIELDS, self.body(body))
        
    def put_data(self):
        pass
        
    def delete_data(self):
        pass
        
        

if __name__=='__main__':
    ws = WebSev()
    url = 'http://www.xiangcloud.com.cn'
    ws.get_data(url)
    
    
    
    
