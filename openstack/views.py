from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os
import json

from utils import HandlePycurl


def test(request):
    """ test request """
    parms = {
        'servername': '192.168.30.127',
        'port': 5000,
    }
    # print request.__class__.__bases__
    url = 'http://%(servername)s:%(port)d/' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url)

    return HttpResponse(context)


def options_test(request):
    """ test request """
    parms = {
        'servername': 'localhost',
        'port': 8090,
        'uri': '/admin/users/1/'
    }
    # print request.__class__.__bases__
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.optionsData(hpc.initCurl(), url)

    return HttpResponse(context)


def head_test(request):
    """ test request """
    parms = {
        'servername': 'localhost',
        'port': 8090,
        'uri': '/admin/users/1/'
    }
    # print request.__class__.__bases__
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.headData(hpc.initCurl(), url)

    return HttpResponse(context)


def put_test(request):
    """ test request """
    parms = {
        'servername': 'localhost',
        'port': 8090,
        'uri': '/admin/users/5/'
    }
    data = {
        "url": "http://localhost:8090/admin/users/5/",
        "username": "zhangliuuuuu",
        "email": "zhangli@sssd.com",
        "is_staff": False
    }
    # print request.__class__.__bases__
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, data=json.dumps(data))

    return HttpResponse(context)


def post_test(request):
    """ post request"""
    head = [
        'Content-Type: application/json',
    ]
    data = {
        "username": "zhangli",
        "email": "zhangli@sssd.com",
        "is_staff": True
    }
    parms = {
        'servername': 'localhost',
        'port': 8090,
        'uri': '/admin/users/'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, data=json.dumps(data))

    return HttpResponse(context)


def patch_test(request):
    """ patch request """
    parms = {
        'servername': 'localhost',
        'port': 8090,
        'uri': '/admin/users/5/'
    }
    data = {
        "url": "http://localhost:8090/admin/users/5/",
        "username": "zhangli",
        "email": "zhangli@sssd.com",
        "is_staff": True
    }
    # print request.__class__.__bases__
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.patchData(hpc.initCurl(), url, data=json.dumps(data))

    return HttpResponse(context)


def addUser(request):
    """Adds a user.

    """
    data = {
        "user": {
            "id": "u1000",
            "name": "jqsmith",
            "email": "john.smith@example.org",
            "enabled": true
        }
    }
    parms = {
        'servername': '192.168.30.127',
        'port': 5000,
        'uri': '/v.2.0/users'
    }
    token_id = 'aaaaaaaaa-addddddddddd-fddddddddf'
    head = [
        'X-Auth-Token: %s' % token_id
    ]
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, data, head)

    return HttpResponse(context)


def obtaindetailUserByName(request):
    """Gets detailed information about a specified user by user name.
            Mothod:GET
    """
    parms = {
        'servername': '192.168.30.127',
        'port': 5000,
        'uri': '/v.2.0/users?name='
    }

    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(url)

    return HttpResponse(context)


def deleteUser(request):
    """ Deletes a user.
            Mothod : DELETE
    """
    parms = {
        'servername': '192.168.30.127',
        'port': 5000,
        'uri': '/v.2.0/users/{userId}'
    }

    url = 'http://%(servername)s:%(port)d%(uri)s' % parms


def obtaindetailUserById(request):
    """  Gets detailed information about a specified user by user ID.
            Mothod; GET
    """
    parms = {
        'servername': '192.168.30.127',
        'port': 5000,
        'uri': '/v2.0/users/{user_id}'
    }

    url = 'http://%(servername)s:%(port)d%(uri)s' % parms


################################openstack api  V3 ######################
