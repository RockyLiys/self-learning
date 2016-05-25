# coding=utf-8
from __future__ import unicode_literals

from django.http import HttpResponse

from openstack.utils import HandlePycurl

try: 
    import simplejson as json
except ImportError: 
    import json


def v2_listComputeTenantLimits(request):
    """ Lists the current absolute and rate limits for a specified project.
            Method:GET
            URI:/v2/{tenant_id}/limits
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/limits' % {
            "tenant_id": req_params.get("tenant_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listComputeExtensions(request):
    """ Lists available extensions.
            Method:GET
            URI:/v2/{tenant_id}/extensions
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/extensions' % {
            "tenant_id": req_params.get("tenant_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailComputeExtension(request):
    """ Gets details about the specified extension.
            Method: GET
            URI:/v2/{tenant_id}/extensions/{alias}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "alias": request.GET.get("alias")
    }

    token_id = '309a7b740ebc4e06b85a02d0ebb70093'

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/extensions/%(alias)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "alias": req_params.get("alias")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listComputeTenantServers(request):
    """ Lists IDs, names, and links for all servers.
            Method:GET
            URI:/v2/{tenant_id}/servers{?changessince,image,flavor,name,status,host,limit,marker}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers' % {
            "tenant_id": req_params.get("tenant_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createComputeTenantServer(request):
    """ Creates a server.
            Method:POST
            URI:/v2/{tenant_id}/servers
    """

    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "imageRef_id": request.POST.get("imageRef_id"),
        "network_uuid": request.POST.get("network_uuid"),
        "security_groups_name": request.POST.get("security_groups_name"),
        "server_name": request.POST.get("server_name"),
        "port": request.POST.get("port", None),
        "tenant_id": request.POST.get("tenant_id")
    }
    if req_params.get("port"):
        data = {
            "server": {
                "name": req_params.get("server_name"),
                "imageRef": req_params.get("imageRef_id"),
                "flavorRef": "2",
                "max_count": 1,
                "min_count": 1,
                "port": req_params.get('port'),
                "security_groups": [
                    {
                        "name": "default"
                    },
                ]
            }
        }
    else:
        data = {
            "server": {
                "name": req_params.get("server_name"),
                "imageRef": req_params.get("imageRef_id"),
                "flavorRef": "2",
                "max_count": 1,
                "min_count": 1,
                "networks": [
                    {
                        "uuid": req_params.get("network_uuid")
                    }
                ],
                "security_groups": [
                    {
                        "name": "default"
                    },
                ]
            }
        }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers' % {
            "tenant_id": req_params.get("tenant_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_detailComputeTenantAllServers(request):
    """ Lists details for all servers.
            Method:GET
            URI:/v2/{tenant_id}/servers/detail{?changes-since,image,flavor,name,status,host,limit,marker}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/detail' % {
            "tenant_id": req_params.get("tenant_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailComputeTenantServer(request):
    """ Gets details for a specified server.
            Method:GET
            URI:/v2/{tenant_id}/servers/{server_id}
    """

    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "server_id": request.GET.get("server_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateComputeTenantServer(request):
    """ Updates the editable attributes of the specified server.
            Method:PUT
            URI:/v2/{tenant_id}/servers/{server_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id")
    }
    # data = {
    #   "server": {
    #       "name": "new-server-test_rocky000000000001111111111"
    #   }
    # }
    # data = {
    #   "server": {
    #       "imageRef": "2b1ad3da-a6ff-4f70-b2a9-a54b0ce3cfd2",
    #   }
    # }
    data = {
        "server": {
            "flavorRef": "5",
        }
    }
    # data = {
    #   "server": {
    #       "networks": [
    #           {
    #               "uuid": "d32019d3-bc6e-4319-9c1d-6722fc136a22"
    #           }
    #       ]
    #   }
    # }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteComputeTenantServer(request):
    """ Deletes a specified server.
            Method:DELETE
            URI:/v2/{tenant_id}/servers/{server_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")


def v2_vncComputeTenantServer(request):
    """ Gets a console for a server instance. 
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id")
    }
    data = {
        "os-getVNCConsole": {
            "type": "novnc"
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/action' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_startComputeTenantServer(request):
    """ Starts  a stopped server and changes its status to ACTIVE
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id")
    }
    data = {
        "os-start": None
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/action' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_stopComputeTenantServer(request):
    """ Stops a running server  and changes its status to SHUTOFF
            Method:
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id")
    }
    data = {
        "os-stop": None
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/action' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showComputeTenantServerMetabata(request):
    """ Shows metadata for a specified server.
            Method:GET
            URI:/v2/{tenant_id}/servers/{server_id}/metadata
    """
    token_id = '075c1a64b472434381349d49b4d0f5a8'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/metadata' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "server_id": "137bb890-3e1f-462d-9e96-1ab7e40521fc"
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createOrReplaceComputeTenantServerMetabata(request):
    """ Creates or replaces metadata items for a specified server.
            Method:PUT
            URI:/v2/{tenant_id}/servers/{server_id}/metadata
    """
    data = {
        "metadata": {
            "name": "test_server_rocky0000002222333"
        },
        "metadata": {
            "name": "test_servdsflkasdfas"
        }
    }
    token_id = '075c1a64b472434381349d49b4d0f5a8'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/metadata' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "server_id": "137bb890-3e1f-462d-9e96-1ab7e40521fc"
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_updateComputeTenantServerMetabata(request):
    """ Updates metadata items by key for a specified server.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/metadata
    """
    data = {
        "metadata": {
            "name": "test_server"
        }
    }
    token_id = '075c1a64b472434381349d49b4d0f5a8'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/metadata' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "server_id": "137bb890-3e1f-462d-9e96-1ab7e40521fc"
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_datailComputeTenantServerMetabata(request):
    """ Shows details for a metadata item by key for a specified server.
            Method:GET
            URI:/v2/{tenant_id}/servers/{server_id}/metadata/{key}
    """
    token_id = '075c1a64b472434381349d49b4d0f5a8'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/metadata/%(key)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "server_id": "137bb890-3e1f-462d-9e96-1ab7e40521fc",
            "key": "sadas"
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_setsComputeTenantServerMetabata(request):
    """ Sets a metadata item by key for a specified server.
            Method:PUT
            URI:/v2/{tenant_id}/servers/{server_id}/metadata/{key}
    """
    pass


def v2_deleteComputeTenantServerMetabata(request):
    """ Deletes a metadata item by key for a specified server.
            Method:DELETE
            URI:/v2/{tenant_id}/servers/{server_id}/metadata/{key}
    """
    pass


def v2_listComputeTenantServerIps(request):
    """ Lists networks and addresses for a specified tenant and server.
            Method:GET
            URI:/v2/{tenant_id}/servers/{server_id}/ips
    """
    pass


def v2_listComputeTenantServerIpsAddresses(request):
    """ Lists addresses for a specified tenant, server, and network.
            Method:GET
            URI:/v2/{tenant_id}/servers/{server_id}/ips/{network_label}
    """
    token_id = 'a78dcddc91bb4ae4a78e20a47c2fcc70'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/ips/%(network_label)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "server_id": "099734ff-3e92-4a3e-bbf3-a1986adab832",
            "network_label": "demo-net"
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_changepasswordComputeTenantServerAction(request):
    """ Changes the password for a server. Specify the changePassword action in the request body.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    data = {
        "changePassword": {
            "adminPass": "foo"
        }
    }

    token_id = '3c1ebb017c76424f81d7e3ae7af8f572'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/action' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "server_id": "137bb890-3e1f-462d-9e96-1ab7e40521fc",
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_rebootComputeTenantServerAction(request):
    """ Reboots the specified server. Specify the reboot action in the request body.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id"),
    }
    data = {
        "reboot": {
            "type": "SOFT"
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/action' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_rebuildComputeTenantServerAction(request):
    """ Rebuilds the specified server. Specify the rebuild action in the request body.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    pass


def v2_resizeComputeTenantServerAction(request):
    """ Resizes the specified server. Specify the resize action in the request body.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id"),
        "flavor_id": request.POST.get("flavor_id"),
    }
    data = {
        "resize": {
            "flavorRef": req_params.get("flavor_id")
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/action' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_confirmResizeComputeTenantServerAction(request):
    """ Confirms a pending resize action. Specify the confirm Resize action in the request body.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    pass


def v2_revertResizeComputeTenantServerAction(request):
    """ Cancels and reverts a pending resize action. Specify the revertResize action in the request body.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    pass


def v2_createImageComputeTenantServerAction(request):
    """ Creates a new image. Specify the createImage action in the request body.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    pass


def v2_listComputeTenantFlavors(request):
    """ Lists IDs, names, and links for available flavors.
            Method:GET
            URI:/v2/{tenant_id}/flavors{?minDisk,minRam,limit,marker}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/flavors' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createComputeTenantFlavor(request):
    """Creates a private flavor.
            Method:POST
            URI:/v2/{tenant_id}/flavors
    """

    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "flavor_name": request.POST.get("flavor_name"),
        "ram_count": request.POST.get("ram_count"),
        "vcpus_count": request.POST.get("vcpus_count"),
        "disk_count": request.POST.get("disk_count"),
        "is_public": request.POST.get("is_public"),
    }
    data = {
        "flavor": {
            "name": req_params.get("flavor_name"),
            "ram": req_params.get("ram_count"),
            "vcpus": req_params.get("vcpus_count"),
            "disk": req_params.get("disk_count"),
            # "id": "10",
            "os-flavor-access:is_public": bool(req_params.get("is_public", "true"))
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/flavors' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head=head)
    return HttpResponse(context)


def v2_detailComputeTenantAllFlavors(request):
    """ Lists all details for available flavors.
            Method:GET
            URI:/v2/{tenant_id}/flavors/detail{?minDisk,minRam,limit,marker}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/flavors/detail' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s?minRam=4096' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailComputeTenantFlavor(request):
    """ Gets details for a specified flavor.
            Method:GET
            URI:/v2/{tenant_id}/flavors/{flavor_id} 
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "flavor_id": request.GET.get("flavor_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/flavors/%(flavor_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "flavor_id": req_params.get("flavor_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listComputeTenantImages(request):
    """ Lists IDs, names, and links for available images.
            Method:GET
            URI:/v2/{tenant_id}/images{?changessince,server,name,status,type,limit,marker}
    """
    token_id = 'a78dcddc91bb4ae4a78e20a47c2fcc70'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/images' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailComputeTenantAllImages(request):
    """ Lists all details for available images.
            Method:GET
            URI:/v2/{tenant_id}/images/detail{?changes-since,server,name,status,type,limit,marker}
    """
    token_id = 'a78dcddc91bb4ae4a78e20a47c2fcc70'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/images/detail' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailComputeTenantImage(request):
    """ Gets details for a specified image.
            Method:GET
            URI:/v2/{tenant_id}/images/{image_id}
    """
    token_id = 'f20a4d27f5a64a25a73d8612d6ff590f'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/images/%(image_id)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "image_id": "e5095bf1-5f6a-4eaf-a74b-d054a7064d83"
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deleteComputeTenantImage(request):
    """ Deletes a specified image.
            Method:DELETE
            URI:/v2/{tenant_id}/images/{image_id}
    """
    pass


def v2_showComputeTenantImagesMetadata(request):
    """ Shows metadata for a specified image.
            Method:GET
            URI:/v2/{tenant_id}/images/{image_id}/metadata
    """
    token_id = 'f20a4d27f5a64a25a73d8612d6ff590f'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/images/%(image_id)s/metadata' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "image_id": "e5095bf1-5f6a-4eaf-a74b-d054a7064d83"
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createOrReplaceComputeTenantImagesMetadata(request):
    """ Creates or replaces metadata for a specified image.
            Method:PUT
            URI:/v2/{tenant_id}/images/{image_id}/metadata
    """
    pass


def v2_updateComputeTenantImagesMetadata(request):
    """ Updates metadata items by key for a specified image.
            Method:POST
            URI:/v2/{tenant_id}/images/{image_id}/metadata
    """
    pass


def v2_detailComputeTenantImagesMetadata(request):
    """ Shows details for a metadata item by key for a specified image
            Method:GET
            URI:/v2/{tenant_id}/images/{image_id}/metadata/{key}
    """
    token_id = 'f20a4d27f5a64a25a73d8612d6ff590f'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/images/%(image_id)s/metadata/%(key)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "image_id": "e5095bf1-5f6a-4eaf-a74b-d054a7064d83",
            "key": ""
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createOrUpdateComputeTenantImagesMetadata(request):
    """ Creates or updates a metadata item by key for a specified image
            Method:PUT
            URI:/v2/{tenant_id}/images/{image_id}/metadata/{key}
    """
    pass


def v2_deleteComputeTenantImagesMetadata(request):
    """ Deletes a metadata item by key for a specified image.
            Method:DELETE
            URI:/v2/{tenant_id}/images/{image_id}/metadata/{key}
    """
    pass


def v2_listComputeTenantOskeypairs(request):
    """ Lists keypairs that are associated with the account.
            Method:GET
            URI:/v2/{tenant_id}/os-keypairs
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-keypairs' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createComputeTenantOskeypairs(request):
    """ Generates  a keypair.
            Method:POST
            URI:/v2/{tenant_id}/os-keypairs
    """

    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "keypair_name": request.POST.get("keypair_name"),
        # "public_key":request.POST.get("public_key")
    }
    data = {
        "keypair": {
            "name": req_params.get("keypair_name"),
            # "public_key": req_params.get("public_key")
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-keypairs' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_importComputeTenantOskeypairs(request):
    """ imports a keypair.
            Method:POST
            URI:/v2/{tenant_id}/os-keypairs
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "keypair_name": request.POST.get("keypair_name"),
        "public_key": request.POST.get("public_key")
    }
    data = {
        "keypair": {
            "name": req_params.get("keypair_name"),
            "public_key": req_params.get("public_key")
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-keypairs' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteComputeTenantOskeypairs(request):
    """ Deletes a keypair.
            Method:DELETE
            URI:/v2/{tenant_id}/os-keypairs/{keypair_name}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "keypair_name": request.POST.get("keypair_name")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-keypairs/%(keypair_name)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "keypair_name": req_params.get("keypair_name")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")


def v2_showComputeTenantOskeypairs(request):
    """ Shows a keypair associated with the account.
            Method:GET
            URI:/v2/{tenant_id}/os-keypairs/{keypair_name}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "keypair_name": request.GET.get("keypair_name")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-keypairs/%(keypair_name)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "keypair_name": req_params.get("keypair_name")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listComputeTenantsOsfloatingipsPools(request):
    """ Lists floating IP pools.
            Method:GET
            URI:/v2/{tenant_id}/os-floating-ip-pools
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-floating-ip-pools' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listComputeTenantsOsfloatingips(request):
    """ Lists floating IP addresses associated with the tenant or account.
            Method:GET
            URI:/v2/{tenant_id}/os-floating-ips
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-floating-ips' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_allocateComputeTenantsOsfloatingips(request):
    """ Allocates a new floating IP address to a tenant or account.
            Method:POST
            URI:/v2/{tenant_id}/os-floating-ips
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "pool_name": request.POST.get("pool_name")
    }
    data = {
        "pool": req_params.get("pool_name")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-floating-ips' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showComputeTenantsOsfloatingips(request):
    """ Shows information for a specified floating IP address.
            Method:GET
            URI:/v2/{tenant_id}/os-floating-ips/{id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "floating_id": request.GET.get("floating_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-floating-ips/%(id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "id": req_params.get("floating_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deallocateComputeTenantsOsfloatingips(request):
    """ Deallocates the floating IP address associated with floating_IP_address_ID.
            Method:DELETE
            URI:/v2/{tenant_id}/os-floating-ips/{id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "floating_id": request.POST.get("floating_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-floating-ips/%(id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "id": req_params.get("floating_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "deallocate successfully")


def v2_addComputeTenantsServersOsfloatingips(request):
    """ Adds a floating IP address to an instance.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id"),
        "floating_address": request.POST.get("floating_address"),
    }
    data = {
        "addFloatingIp": {
            "address": req_params.get("floating_address")
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/action' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_removeComputeTenantsServersOsfloatingips(request):
    """ Removes a floating IP from an instance.
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/action
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id"),
        "floating_address": request.POST.get("floating_address"),
    }
    data = {
        "removeFloatingIp": {
            "address": req_params.get("floating_address")
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/action' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_attachComputeTenantServerVolume(request):
    """ Attaches a volume to the specified server .
            Method:POST
            URI:/v2/{tenant_id}/servers/{server_id}/os-volume_attachments
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id"),
        "volume_id": request.POST.get("volume_id"),
    }
    data = {
        "volumeAttachment": {
            "volumeId": req_params.get("volume_id"),
            "device": "/dev/sdd"
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/os-volume_attachments' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_detachComputeTenantServerVolume(request):
    """ Detaches the specified volume from a specified server.
            Method:DELETE
            URI:/v2/{tenant_id}/servers/{server_id}/os-volume_attachments/{attachment_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id"),
        "attachment_id": request.POST.get("attachment_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/os-volume_attachments/%(attachment_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id"),
            "attachment_id": req_params.get("attachment_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head=head)
    return HttpResponse(context)


def v2_listComputeTenantsOshosts(request):
    """ Lists hosts.
            Method:GET
            URI:/v2/{tenant_id}/os-hosts{?service,zone}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-hosts' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_showComputeTenantsOshosts(request):
    """ Shows information for a specified host.
            Method:GET
            URI:/v2/{tenant_id}/os-hosts/{host_name}
    """
    pass


def v2_enableOrputComputeTenantsOshosts(request):
    """ Enables a host or puts it in maintenance mode.
            Method:PUT
            URI:/v2/{tenant_id}/os-hosts/{host_name}
    """
    pass


def v2_startComputeTenantsOshosts(request):
    """ Starts a host.
            Method:GET
            URI:/v2/{tenant_id}/os-hosts/{host_name}/startup
    """
    pass


def v2_shutdownComputeTenantsOshosts(request):
    """ Shuts down a host.
            Method:GET
            URI:/v2/{tenant_id}/os-hosts/{host_name}/shutdown
    """
    pass


def v2_rebootComputeTenantsOshosts(request):
    """ Reboots a host.
            Method:GET
            URI:/v2/{tenant_id}/os-hosts/{host_name}/reboot

    """
    pass


def v2_createOsInterfaceComputeTenantsServers(request):
    """ Creates a port interface and uses it to attach a port to a server instance.
        Method:POST
        URI:/v2.1/​{tenant_id}​/servers/​{server_id}​/os-interface
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id"),
        "port_id": request.POST.get("port_id"),
    }
    data = {
        "interfaceAttachment": {
            "port_id": req_params.get('port_id')
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/os-interface' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)  

def v2_listOsInterfaceComputeTenantsServers(request):
    """ Lists port interfaces that are attached to a server.
        Method:GET
        URI:/v2.1/​{tenant_id}​/servers/​{server_id}​/os-interface
    """ 
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "server_id": request.GET.get("server_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/os-interface'.strip() % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)    

def v2_showAttachmentOsInterfaceComputeTenantsServers(request):
    """ Shows details for a port interface that is attached to a server.
        Method:GET
        URI:/v2.1/​{tenant_id}​/servers/​{server_id}​/os-interface/​{attachment_id}​
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "server_id": request.GET.get("server_id"),
        "attachment_id": request.GET.get("attachment_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/​%(server_id)s​/os-interface/%(attachment_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id"),
            "attachment_id": req_params.get("attachment_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)   

def v2_deleteAttachmentOsInterfaceComputeTenantsServers(request):
    """ Detaches a port interface.
        Method:DELETE
        URI:/v2.1/​{tenant_id}​/servers/​{server_id}​/os-interface/​{attachment_id}​
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "server_id": request.POST.get("server_id"),
        "attachment_id": request.POST.get("attachment_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/os-interface/%(attachment_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get("server_id"),
            "attachment_id": req_params.get("attachment_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head=head)
    return HttpResponse(context)


def v2_DefaultsComputeTenantsQuota(request):
    """List default quotas for tenant
        Lists the default quotas for a project or a project and a user.
        Method: GET
        URI: /v2.1/​{admin_tenant_id}​/os-quota-sets/​{tenant_id}​/defaults
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "admin_tenant_id": request.GET.get("admin_tenant_id"),
        "tenant_id": request.GET.get("tenant_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(admin_tenant_id)s/os-quota-sets/%(tenant_id)s/defaults' % {
            "admin_tenant_id": req_params.get("admin_tenant_id"),
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)   

def v2_DetailComputeTenantsQuota(request):
    """ List quotas with details
        Lists quotas with details for a project or a project and a user.
        Method:GET
        URI:/v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}/detail
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "admin_tenant_id": request.GET.get("admin_tenant_id"),
        "tenant_id": request.GET.get("tenant_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(admin_tenant_id)s/os-quota-sets/%(tenant_id)s/detail' % {
            "admin_tenant_id": req_params.get("admin_tenant_id"),
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)   

def v2_updateComputeTenantsQuota(request):
    """ Update quotas
        Update the quotas for a project or a project and a user.
        Method:PUT
        URI:/v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}​
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "admin_tenant_id": request.POST.get("admin_tenant_id"),
        "tenant_id": request.POST.get("tenant_id"),
        "key_pairs": request.POST.get("key_pairs_count"),
    }
    print req_params
    data = {
        "quota_set": {
            # "force": True,
            "tenant_id": req_params.get('tenant_id'),
            "key_pairs": int(req_params.get('key_pairs'))
        }
    }
    print data
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(admin_tenant_id)s/os-quota-sets/%(tenant_id)s' % {
            "admin_tenant_id": req_params.get("admin_tenant_id"),
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)

def v2_listComputeTenantOsSecuritygroups(request):
    """ Lists security groups.
        Method: GET
        URI: /v2.1/{tenant_id}/os-security-groups
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-security-groups' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)

def v2_createComputeTenantOsSecuritygroups(request):
    """ Creates a security group.
        Method: POST
        URI: /v2.1/{tenant_id}/os-security-groups
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "security_group_name": request.POST.get("security_group_name"),
        "description": request.POST.get("description"),
    }
    data = {
        "security_group": {
            "name": req_params.get('security_group_name'),
            "description": req_params.get('description')
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-security-groups' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)  

def v2_detailComputeTenantOsSecuritygroups(request):
    """
        Method: GET
        URI:/v2.1/{tenant_id}/os-security-groups/{security_group_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "security_group_id": request.GET.get("security_group_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-security-groups/%(security_group_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "security_group_id": req_params.get('security_group_id')
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)

def v2_updateComputeTenantOsSecuritygroups(request):
    """ Updates a security group.
        Method: PUT
        URI: /v2.1/{tenant_id}/os-security-groups/{security_group_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "security_group_id": request.POST.get("security_group_id"),
        "security_group_name": request.POST.get('security_group_name'),
        "description": request.POST.get('description'),
    }
    data = {
        "security_group": {
            "name": req_params.get('security_group_name'),
            "description": req_params.get('description')
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-security-groups/%(security_group_id)s' % {
            "tenant_id": req_params.get('tenant_id'),
            "security_group_id": req_params.get('security_group_id')
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)

def v2_deleteComputeTenantOsSecuritygroups(request):
    """
        Method:DELETE
        URI: /v2.1/{tenant_id}/os-security-groups/{security_group_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "security_group_id": request.POST.get("security_group_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-security-groups/%(security_group_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "security_group_id": req_params.get("security_group_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")

def v2_listComputeTenantServerOsSecuritygroups(request):
    """ Lists security groups for a server.
        Method: GET
        URI: /v2.1/{tenant_id}/servers/{server_id}/os-security-groups
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "server_id": request.GET.get("server_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/servers/%(server_id)s/os-security-groups' % {
            "tenant_id": req_params.get("tenant_id"),
            "server_id": req_params.get('server_id')
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)

def v2_createComputeTenantOsSecuritygroupsRules(request):
    """ Creates a rule for a security group.
        Method: POST
        URI: /v2.1/{tenant_id}/os-security-group-rules
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),

        "from_port": request.POST.get("from_port"),
        "to_port": request.POST.get("to_port"),
        "cidr": request.POST.get("cidr"),
        "ip_protocol": request.POST.get("ip_protocol"),
        "parent_group_id": request.POST.get("parent_group_id"),
    }
    data = {
        "security_group_rule": {
            "from_port": req_params.get('from_port'),
            "ip_protocol": req_params.get('ip_protocol'),
            "to_port": req_params.get('to_port'),
            "cidr": req_params.get('cidr'),
            "parent_group_id": req_params.get('parent_group_id')
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-security-group-rules' % {
            "tenant_id": req_params.get("tenant_id"),
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)  

def v2_deleteComputeTenantOsSecuritygroupsRules(request):
    """ Deletes a security group rule.
        Method: DELETE
        URI: /v2.1/{tenant_id}/os-security-group-rules/{security_group_rule_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "security_group_rule_id": request.POST.get("security_group_rule_id")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2/%(tenant_id)s/os-security-group-rules/%(security_group_rule_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "security_group_rule_id": req_params.get("security_group_rule_id")
        },
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")




