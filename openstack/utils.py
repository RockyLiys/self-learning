# coding=utf-8
# from __future__ import unicode_literals
# 2015年11月06日 星期五 13时33分30秒 

import urllib
import pycurl
import StringIO
import json
import re



class HandlePycurl(object):

    """docstring for HandlePycurl"""

    def __init__(self):
        super(HandlePycurl, self).__init__()

    def initCurl(self):
        """init pycurl instance"""
        c = pycurl.Curl()
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        # c.setopt(pycurl.VERBOSE,True)
        return c

    def getData(self, curl, url, head=[]):
        """ GET data From url """
        head += [
            'Content-Type: application/json',
            'Accept:*/*',
        ]
        print url
        buf = StringIO.StringIO()
        curl.setopt(pycurl.URL, urllib.unquote(url))
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        # curl.setopt(pycurl.HEADER,True)
        curl.setopt(pycurl.HTTPHEADER, head)
        curl.perform()
        the_page = buf.getvalue()
        buf.close()
        return curl.getinfo(curl.HTTP_CODE), the_page

    def postData(self, curl, url, data={}, head=[], v3=False):
        """ POST data From url """
        head += [
            'Content-Type: application/json',
            'Accept:*/*',
        ]
        buf = StringIO.StringIO()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.POSTFIELDS, data)  # data is json
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.HTTPHEADER, head)
        if v3:
            curl.setopt(pycurl.HEADER, True)
        curl.perform()
        the_page = buf.getvalue()
        # print the_page
        if v3:
            try:
                header_size = curl.getinfo(curl.HEADER_SIZE)
                head = the_page[:header_size]
                print head
                s = [v for v in head.split('\r\n') if 'X-Subject-Token' in v][0].split(':')
                ret_json = json.loads(the_page[header_size:])
                ret_json["token"]["token_id"] = s[1].strip()
                buf.close()
                return json.dumps(ret_json)
            except Exception, e:
                print e
        buf.close()
        return the_page

    def putData(self, curl, url, data={}, head=[]):
        """ PUT method data """

        head += [
            'Content-Type: application/json',
            'Content-Length: %d' % len(data),
            'X-HTTP-Method-Override: PUT'
        ]

        buf = StringIO.StringIO()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.CUSTOMREQUEST, "PUT")
        # curl.setopt(pycurl.PUT,1)
        # curl.setopt(pycurl.UPLOAD, 1)
        curl.setopt(pycurl.HTTPHEADER, head)
        # curl.setopt(pycurl.VERBOSE,True)
        if data:
            curl.setopt(pycurl.POSTFIELDS, data)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.perform()
        the_page = buf.getvalue()
        buf.close()
        return the_page

    def deleteData(self, curl, url, head=[]):
        """ delete data """
        head += [
            'Content-Type: application/json',
        ]
        buf = StringIO.StringIO()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.CUSTOMREQUEST, "DELETE")
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.HTTPHEADER, head)
        curl.perform()
        the_page = buf.getvalue()
        buf.close()
        return the_page

    def headData(self, curl, url, head=[]):
        """ HEAD Data """
        head += [
            'Content-Type: application/json'
        ]

        buf = StringIO.StringIO()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.CUSTOMREQUEST, "HEAD")
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.HTTPHEADER, head)
        curl.perform()
        the_page = buf.getvalue()
        buf.close()
        return the_page

    def optionsData(self, curl, url, head=[]):
        """
                options method Data
        """
        head += [
            'Content-Type: application/json'
        ]
        buf = StringIO.StringIO()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.CUSTOMREQUEST, "OPTIONS")
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.HTTPHEADER, head)
        curl.perform()
        the_page = buf.getvalue()
        buf.close()
        return the_page

    def patchData(self, curl, url, data, head=[]):
        """ PATCH data """
        # return self.putData(curl,url,data,head)

        head += [
            'Content-Type: application/json',
            'Content-Length: %d' % len(data),
            'X-HTTP-Method-Override: PATCH'
        ]

        buf = StringIO.StringIO()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.CUSTOMREQUEST, "PATCH")
        # curl.setopt(pycurl.PUT,1)
        # curl.setopt(pycurl.UPLOAD, 1)
        curl.setopt(pycurl.HTTPHEADER, head)
        # curl.setopt(pycurl.VERBOSE,True)
        curl.setopt(pycurl.POSTFIELDS, data)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.perform()
        the_page = buf.getvalue()
        buf.close()
        return the_page
