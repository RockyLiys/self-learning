from __future__ import unicode_literals
from django.http import HttpResponse

from openstack.utils import HandlePycurl

import json


def v2_createImages(request):
    """ Creates a virtual machine (VM) image. (Since Image APIv2.0.)
        Method:POST
        URI:/v2/images
    """
    print request.POST

    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "image_name": request.POST.get("image_name"),
        "image_file": request.POST.get("image_file")
    }
    data = {
        "name": req_params.get("image_name"),
        "description": req_params.get("image_desc", req_params.get("image_name")),
        "container_format": req_params.get("container_format", "bare"),
        "disk_format": req_params.get("disk_format", "qcow2"),
        "file": req_params.get("image_file"),
        "schema": "/v2/schemas/image",
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8777,
        'uri': '/v2.0/images'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_listImages(request):
    """ Lists public virtual machine (VM) images. (Since Image APIv2.0.)
        Method:GET
        URI:/v2/images{?limit,marker,name,visibility,member_status,owner,status,size_min,size_max,sort_key,sort_dir,tag}
    """

    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9292,
        'uri': '/v2.0/images'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailImages(request):
    """ Gets details for a specified image. (Since Image API v2.0.)
            Method:GET
            URI:/v2/images/{image_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "image_id"	: request.GET.get("image_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9292,
        'uri': '/v2.0/images/%(image_id)s' % {
            "image_id": req_params.get("image_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateImages(request):
    """ Updates a specified image. (Since Image API v2.0.)
        Method:PATCH
        URI:/v2/images/{image_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "image_id": request.POST.get("image_id")
    }
    data = [
        {
            "op": "replace",
            "path": "/name",
            "value": "Fedora 17"
        },
        {
            "op": "replace",
            "path": "/tags",
            "value": [
                "fedora",
                "beefy"
            ]
        }
    ]

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9292,
        'uri': '/v2.0/images/%(image_id)s' % {
            "image_id": req_params.get("image_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.patchData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteImages(request):
    """ Deletes a specified image. (Since Image API v2.0.)
        Method:DELETE
        URI:/v2/images/{image_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "image_id": request.POST.get("image_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9292,
        'uri': '/v2.0/images/%(image_id)s' % {
            "image_id": req_params.get("image_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_uploadImagesFile(request):
    """ Uploads binary image data. (Since Image API v2.0.)
        Method:PUT
        URI:/v2/images/{image_id}/file
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "image_id": request.POST.get("image_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
        "Content-Type: application/octet-stream"
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9292,
        'uri': '/v2/images/%(image_id)s/file' % {
            "image_id": req_params.get("image_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_downloadImagesFile(request):
    """ Downloads binary image data. (Since Image API v2.0.)
        Method:GET
        URI:/v2/images/{image_id}/file
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "image_id": request.POST.get("image_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9292,
        'uri': '/v2/images/%(image_id)s/file' % {
            "image_id": req_params.get("image_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_addImagesTags(request):
    """ Adds a specified tag to a specified image. (Since Image APIv2.0.)
        Method:PUT
        URI:/v2/images/{image_id}/tags/{tag}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "image_id": request.POST.get("image_id"),
        "tag_name": request.POST.get("tag_name")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9292,
        'uri': '/v2/images/%(image_id)s/tags/%(tag)s' % {
            "image_id": req_params.get("image_id"),
            "tag_name": req_params.get("tag_name")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deleteImagesTags(request):
    """ Deletes a specified tag from a specified image. (Since Image API v2.0.)
        Method:DELETE
        URI:/v2/images/{image_id}/tags/{tag}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "image_id": request.POST.get("image_id"),
        "tag_name": request.POST.get("tag_name")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9292,
        'uri': '/v2/images/%(image_id)s/tags/%(tag)s' % {
            "image_id": req_params.get("image_id"),
            "tag_name": req_params.get("tag_name")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_addImagesMembers(request):
    """ Adds a specified tenant ID as an image member. (Since Image API v2.1.)
            Method:POST
            URI:/v2/images/{image_id}/members
    """
    pass


def v2_listImagesMembers(request):
    """ Lists the tenants with whom this image has been shared.(Since Image API v2.1.)
            Method:GET
            URI:/v2/images/{image_id}/members
    """
    token_id = 'ecbf0a4e12ef4649adf7a8f5f39718b7'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9292,
        'uri': '/v2.0/images/%(image_id)s/members' % {
            "image_id": "33139f93-b2d0-4b4b-99c3-f40778d624c9"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailImagesMembers(request):
    """ Shows image member details.
            Method:GET
            URI:/v2/images/{image_id}/members/{member_id}
    """
    token_id = 'ecbf0a4e12ef4649adf7a8f5f39718b7'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9292,
        'uri': '/v2.0/images/%(image_id)s/members/%(member_id)s' % {
            "image_id": "33139f93-b2d0-4b4b-99c3-f40778d624c9",
            "member_id": "aaaaaaaaaaaa-a------------dd-----ads--f-s-d-f-a"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deleteImagesMembers(request):
    """ Deletes a specified tenant ID from the member list of the specified image. (Since Image API v2.1.)
            Method: DELETE
            URI:/v2/images/{image_id}/members/{member_id}
    """
    token_id = 'ecbf0a4e12ef4649adf7a8f5f39718b7'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9292,
        'uri': '/v2.0/images/%(image_id)s/members/%(member_id)s' % {
            "image_id": "33139f93-b2d0-4b4b-99c3-f40778d624c9",
            "member_id": "aaaaaaaaaaaa-a------------dd-----ads--f-s-d-f-a"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateImagesMembers(request):
    """ Sets the specified status for the specified member of the specified image. (Since Image API v2.1.)
            Method:
            URI:/v2/images/{image_id}/members/{member_id}
    """
    pass


def v2_getImagesSchemas(request):
    """ Gets a json-schema document that represents an images entity. (Since Images v2.0.)
            Method:GET
            URI:/v2/schemas/images
    """
    token_id = 'c72a23c2e61241748c2eaa063126fcb0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9292,
        'uri': '/v2/schemas/images'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_getImagesSchema(request):
    """ Gets a json-schema document that represents an image entity. (Since Images v2.0.)
            Method:GET
            URI:/v2/schemas/image
    """
    token_id = 'c72a23c2e61241748c2eaa063126fcb0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9292,
        'uri': '/v2/schemas/image'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_getImagesSchemasMembers(request):
    """ Gets a json-schema document that represents an image members entity. (Since Images v2.1.)
            Method:GET
            URI:/v2/schemas/members
    """
    token_id = 'c72a23c2e61241748c2eaa063126fcb0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9292,
        'uri': '/v2/schemas/members'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_getImagesSchemasMember(request):
    """ Gets a json-schema document that represents an image member entity. (Since Images v2.1.)
            Method:GET
            URI:/v2/schemas/member
    """
    token_id = 'c72a23c2e61241748c2eaa063126fcb0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9292,
        'uri': '/v2/schemas/member'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)
