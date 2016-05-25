# coding=utf-8

from keystoneclient.v2_0 import client
from glanceclient import Client


def auth_token(username, password, tenant_name, auth_url):

    keystone = client.Client(username=username, password=password, tenant_name=tenant_name, auth_url=auth_url)

    return keystone.auth_token


def glance(version, os_image_endpoint, token):

    return Client(version, endpoint=os_image_endpoint, token=token)

if __name__ == '__main__':
    username = 'admin'
    password = 'password'
    tenant_name = 'admin'
    auth_url = 'http://192.168.30.59:5000/v2.0'

    os_image_endpoint = 'http://192.168.30.59:9292/'
    version = '2'
    token = auth_token(username, password, tenant_name, auth_url)

    glance_object = glance(version, os_image_endpoint, token)

    print glance_object.version
