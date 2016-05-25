#from __future__ import unicode_literals
# coding=utf-8
from django.http import HttpResponse

from openstack.utils import HandlePycurl

import json


def v2_listNetworks(request):
    """Lists networks that are accessible to the tenant who submits the request.
            Method:GET
            URI:/v2.0/networks
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
        'port': 9696,
        'uri': '/v2.0/networks'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworks(request):
    """ Creates a network.
            Method: POST
            URI:/v2.0/networks
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "network_name": request.POST.get("network_name")
    }

    data = {
        "network": {
            "name": req_params.get("network_name"),
            "admin_state_up": True
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/networks'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_createMultipleNetworks(request):
    """ Creates multiple networks in a single request.
            Method:POST
            URI:/v2.0/networks
    """
    data = {
        "networks": [
            {
                "name": "sample_network3",
                "admin_state_up": True
            },
            {
                "name": "sample_network4",
                "admin_state_up": True
            }
        ]
    }
    token_id = '3562560ae30c4002a2b61a2c75828cbd'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/networks'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworks(request):
    """ Shows information for a specified network.
            Method: GET
            URI:/v2.0/networks/{network_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "network_id": request.GET.get("network_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/networks/%(network_id)s' % {
            "network_id": req_params.get("network_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworks(request):
    """ Updates a specified network.
            Method:PUT
            URI:/v2.0/networks/{network_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "network_id": request.POST.get("network_id"),
        "network_name": request.POST.get("network_name"),
    }

    data = {
        "network": {
            "name": req_params.get("network_name")
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/networks/%(network_id)s' % {
            "network_id": req_params.get("network_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteNetworks(request):
    """ Deletes a specified network and its associated resources.
            Method:DELETE
            URI:/v2.0/networks/{network_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "network_id": request.POST.get("network_id"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/networks/%(network_id)s' % {
            "network_id": req_params.get("network_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")


def v2_listNetworksSubnets(request):
    """ Lists subnets to which the specified tenant has access.
        Method:GET
        URI:/v2.0/subnets{?display_name,network_id,gateway_ip,ip_version,cidr,id,enable_dhcp,ipv6_ra_mode,ipv6_address_mode}
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
        'port': 9696,
        'uri': '/v2.0/subnets'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksSubnets(request):
    """ Creates a subnet on a specified network.
            Method: POST
            URI:/v2.0/subnets
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "network_id": request.POST.get("network_id"),
        "subnet_name": request.POST.get("subnet_name"),
        "ip_version": request.POST.get("ip_version"),
        "cidr": request.POST.get("cidr")

    }

    data = {
        "subnet": {
            "name": req_params.get("subnet_name"),
            "network_id": req_params.get("network_id"),
            "ip_version": req_params.get("ip_version"),
            "cidr": req_params.get("cidr")
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/subnets'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_createNetworksMultipleSubnets(request):
    """ Creates multiple subnets in a single request. Specify a list of subnets in the request body.
            Method:POST
            URI:/v2.0/subnets
    """
    data = {
        "subnets": [
            {
                "name": "rocky000000333333",
                "cidr": "192.168.199.0/24",
                "ip_version": 4,
                "network_id": "3537a85e-f76a-4210-9f65-d09d8672514f"
            },
            {
                "name": "rocky00000wweeeee",
                "cidr": "10.56.4.0/24",
                "ip_version": 4,
                "network_id": "3537a85e-f76a-4210-9f65-d09d8672514f"
            }
        ]
    }
    token_id = '838ee0a420c2439dba382cdf41f52078'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/subnets'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksSubnets(request):
    """ Shows information for a specified subnet.
            Method:GET
            URI:/v2.0/subnets/{subnet_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "subnet_id": request.GET.get("subnet_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/subnets/%(subnet_id)s' % {
            "subnet_id": req_params.get("subnet_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksSubnets(request):
    """ Updates a specified subnet.
            Method:PUT
            URI:/v2.0/subnets/{subnet_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "subnet_id": request.POST.get("subnet_id"),
        "subnet_name": request.POST.get("subnet_name")
    }
    data = {
        "subnet": {
            "name": req_params.get("subnet_name")
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/subnets/%(subnet_id)s' % {
            "subnet_id": req_params.get("subnet_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteNetworksSubnets(request):
    """ Deletes a specified subnet.
            Method:DELETE
            URI:/v2.0/subnets/{subnet_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "subnet_id": request.POST.get("subnet_id"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/subnets/%(subnet_id)s' % {
            "subnet_id": req_params.get("subnet_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")


def v2_listNetworksPorts(request):
    """ Lists ports to which the tenant has access.
        Method:GET
        URI:/v2.0/ports{?status,display_name,admin_state,network_id,device_owner,mac_address,port_id,security_groups,device_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "device_id": request.GET.get('router_id')
    }
    if req_params.has_key("device_id"):
        query = "?device_id=%s" % req_params.get('device_id')
    else:
        query = ''

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/ports%s' % query
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksPorts(request):
    """ Creates a port on a specified network.
        Method:POST
        URI:/v2.0/ports
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "network_id": request.POST.get("network_id"),
        "port_name": request.POST.get("port_name"),
        "subnet_id": request.POST.get('subnet_id'),
        'ip_address': request.POST.get("ip_address")
    }

    data = {
        "port": {
            "network_id": req_params.get("network_id"),
            "name": req_params.get("port_name"),
            "admin_state_up": True,
            "fixed_ips": [{
                "subnet_id": req_params.get("subnet_id"),
                "ip_address": req_params.get("ip_address")
            }]
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/ports'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_createNetworksMultiplePorts(request):
    """ Creates multiple ports in a single request. Specify a list of ports in the request body.
            Method:POST
            URI:/v2.0/ports
    """
    data = {
        "ports": [
            {
                "name": "sample_port_1",
                "admin_state_up": True,
                "network_id": "3537a85e-f76a-4210-9f65-d09d8672514f"
            },
            {
                "name": "sample_port_2",
                "admin_state_up": True,
                "network_id": "3537a85e-f76a-4210-9f65-d09d8672514f"
            }
        ]
    }
    token_id = '838ee0a420c2439dba382cdf41f52078'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/ports'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksPorts(request):
    """ Shows information for a specified port.
            Method: GET
            URI:/v2.0/ports/{port_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "port_id": request.GET.get("port_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/ports/%(port_id)s' % {
            "port_id": req_params.get("port_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksPorts(request):
    """ Updates a specified port.
            Method:PUT
            URI:/v2.0/ports/{port_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "port_id": request.POST.get("port_id"),
        "port_name": request.POST.get("port_name", None),
        "security_group_id": request.POST.get('security_group_id')
    }
    if not req_params.get('port_name'):  # update security_groups
        data = {
            "port": {
                # "name": req_params.get("port_name"),
                "admin_state_up": True,
                # "device_owner": "network:router_interface",
                # "device_id": "17bd04a4-c869-485d-842e-c7352f4f0226",
                # "fixed_ips": [{
                #     "subnet_id": "552e7d57-2a89-4580-8597-f9142e6f875b",
                #     "ip_address": "10.10.10.10"
                # }
                # ]
                'security_groups': [
                    req_params.get('security_group_id')
                ] 

            }
        }
    else:  # rename 
        data = {
            "port": {
                "name": req_params.get("port_name"),
                "admin_state_up": True,
                # "device_owner": "network:router_interface",
                # "device_id": "17bd04a4-c869-485d-842e-c7352f4f0226",
                # "fixed_ips": [{
                #     "subnet_id": "552e7d57-2a89-4580-8597-f9142e6f875b",
                #     "ip_address": "10.10.10.10"
                # }
                # ]
                # 'security_groups': [
                #     req_params.get('security_group_id')
                # ] 

            }
        }
    print data
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/ports/%(port_id)s' % {
            "port_id": req_params.get("port_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteNetworksPorts(request):
    """ Deletes a specified port.
            Method:DELETE
            URI:/v2.0/ports/{port_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "port_id": request.POST.get("port_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/ports/%(port_id)s' % {
            "port_id": req_params.get("port_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete  successfully")


#################################################################
#                           Extensions
#################################################################


def v2_listNetworksExtensions(request):
    """ Lists available Networking API extensions.
            Method:GET
            URI:/v2.0/extensions
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
        'port': 9696,
        'uri': '/v2.0/extensions'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailNetworksExtensions(request):
    """ Gets detailed information for a specified extension.
            Method:GET
            URI:/v2.0/extensions/{alias}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "alias": request.GET.get("alias")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/extensions/%(alias)s' % {
            "alias": req_params.get("alias")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_showNetworksQuotas(request):
    """ Shows quotas for a specified tenant.
            Method:GET
            URI:/v2.0/quotas
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
        'port': 9696,
        'uri': '/v2.0/quotas'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksQuotas(request):
    """ Updates quotas for a specified tenant. Use when non-default quotas are desired.
            Method:PUT
            URI:/v2.0/quotas/{tenant_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "subnet_count": request.POST.get("subnet_count"),
        "router_count": request.POST.get("router_count"),
        "network_count": request.POST.get("network_count"),
        "floatingip_count": request.POST.get("floatingip_count"),
        "port_count": request.POST.get("port_count"),
    }

    data = {
        "quota": {
            "subnet": 40,
            "router": 50,
            "network": 10,
            "floatingip": 30,
            "port": 30
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.remotehost,
        'port': 9696,
        'uri': '/v2.0/quotas/%(tenant_id)s' % {
            "tenant_id": req_params.tenant_id
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_resetNetworksQuotas(request):
    """ Resets quotas to default values for a specified tenant.
            Method:DELETE
            URI:/v2.0/quotas/{tenant_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/quotas/%(tenant_id)s' % {
            "tenant_id": req_params.get("tenant_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listNetworksSecuritygroups(request):
    """ Lists OpenStack Networking security groups to which the specified tenant has access.
            Method:GET
            URI:/v2.0/security-groups
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
        'port': 9696,
        'uri': '/v2.0/security-groups'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksSecuritygroups(request):
    """ Creates an OpenStack Networking security group.
            Method:POST
            URI:/v2.0/security-groups
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "security_group_name": request.POST.get("security_group_name"),
        "security_group_description": request.POST.get("security_group_description")
    }
    data = {
        "security_group": {
            "name": req_params.get("security_group_name"),
            "description": req_params.get("security_group_description")
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/security-groups'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksSecuritygroups(request):
    """ Shows details for a specified security group.
            Method:GET
            URI:/v2.0/security-groups/{security_group_id}{?verbose,fields}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "security_group_id": request.GET.get("security_group_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/security-groups/%(security_group_id)s' % {
            "security_group_id": req_params.get("security_group_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deleteNetworksSecuritygroups(request):
    """ Deletes an OpenStack Networking security group.
            Method:DELETE
            URI:/v2.0/security-groups/{security_group_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "security_group_id": request.POST.get("security_group_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/security-groups/%(security_group_id)s' % {
            "security_group_id": req_params.get("security_group_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")


def v2_listNetworksSecuritygroupsRules(request):
    """ Lists a summary of all OpenStack Networking security group rules that the specified tenant can access.
            Method:GET
            URI:/v2.0/security-group-rules
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
        'port': 9696,
        'uri': '/v2.0/security-group-rules'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksSecuritygroupsRules(request):
    """ Creates an OpenStack Networking security group rule.
            Method:POST
            URI:/v2.0/security-group-rules
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "security_group_id" : request.POST.get("security_group_id")
    }
    data = {
        "security_group_rule": {
            "direction": "ingress",
            "port_range_min": "80",
            "ethertype": "IPv4",
            "port_range_max": "80",
            "protocol": "tcp",
            "remote_group_id": req_params.get("security_group_id"),
            "security_group_id": req_params.get("security_group_id")
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/security-group-rules'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksSecuritygroupsRules(request):
    """ Shows detailed information for a specified security group rule.
            Method:GET
            URI:/v2.0/security-group-rules/{rules_security_groups_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "rules_security_groups_id"  : request.GET.get("rules_security_groups_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/security-group-rules/%(rules_security_groups_id)s' % {
            "rules_security_groups_id": req_params.get("rules_security_groups_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deleteNetworksSecuritygroupsRules(request):
    """ Deletes a specified rule from a OpenStack Networking security group.
            Method:DELETE
            URI:/v2.0/security-group-rules/{rules_security_groups_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "rules_security_groups_id": request.POST.get("rules_security_groups_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/security-group-rules/%(rules_security_groups_id)s' % {
            "rules_security_groups_id": req_params.get("rules_security_groups_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listNetworksRouters(request):
    """ Lists logical routers that are accessible to the tenant who submits the request.
            Method:GET
            URI:/v2.0/routers
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
        'port': 9696,
        'uri': '/v2.0/routers'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksRouters(request):
    """ Creates a logical router.
            Method:POST
            URI:/v2.0/routers
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "network_id": request.POST.get("network_id"),
        "router_name": request.POST.get("router_name"),
    }
    data = {
        "router": {
            "name": req_params.get("router_name"),
            # "external_gateway_info": {
            #     "network_id": req_params.get("network_id")
            # },
            "admin_state_up": True
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/routers'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_detailNetworksRouters(request):
    """ Shows details for a specified router.
            Method:GET
            URI:/v2.0/routers/{router_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "router_id": request.GET.get("router_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/routers/%(router_id)s' % {
            "router_id": req_params.get("router_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksRouters(request):
    """ Updates a logical router.
            Method:PUT
            URI:/v2.0/routers/{router_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "router_id": request.POST.get("router_id"),
        "router_name": request.POST.get("router_name"),
        "network_id": request.POST.get("network_id"),
    }
    data = {
        "router": {
            # "name": req_params.get("router_name"),
            "external_gateway_info": None
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/routers/%(router_id)s' % {
            "router_id": req_params.get("router_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteNetworksRouters(request):
    """ Deletes a logical router and, if present, its external gateway interface.
            Method:DELETE
            URI:/v2.0/routers/{router_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "router_id": request.POST.get("router_id"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/routers/%(router_id)s' % {
            "router_id": req_params.get("router_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")


def v2_addNetworksRoutersInterfaces(request):
    """ Adds an internal interface to a logical router.
            Method:PUT
            URI:/v2.0/routers/{router_id}/add_router_interface
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "router_id": request.POST.get("router_id"),
        "subnet_id": request.POST.get("subnet_id"),
        "port_id": request.POST.get("port_id")
    }

    data = {
        # "subnet_id": req_params.get("subnet_id"),
        "port_id": req_params.get("port_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/routers/%(router_id)s/add_router_interface' % {
            "router_id": req_params.get("router_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_removeNetworksRoutersInterfaces(request):
    """ Removes an internal interface from a logical router.
            Method:PUT
            URI:/v2.0/routers/{router_id}/remove_router_interface
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "router_id": request.POST.get("router_id"),
    }
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "router_id": request.POST.get("router_id"),
        "subnet_id": request.POST.get("subnet_id"),
        "port_id": request.POST.get("port_id"),
    }

    data = {
        # "subnet_id": req_params.get("subnet_id"),
        "port_id": req_params.get("port_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/routers/%(router_id)s/remove_router_interface'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)
    
    
def v2_addExternalNetworksRoutersSetGateway(request):
    """ add external_gateway_info to router
        Method:PUT
        URI:/v2.0/routers/{router_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "router_id": request.POST.get("router_id"),
        "network_id": request.POST.get("network_id")
    }
    data ={
        "router": {
            "external_gateway_info": {
                "network_id": req_params.get('network_id'),
                "enable_snat": "True",
            }
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/routers/%(router_id)s' % {
            "router_id": req_params.get("router_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)
    
def v2_clearExternalNetworksRoutersClearGateway(request):
    """ add external_gateway_info to router
        Method: PUT
        URI: /v2.0/routers/{router_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "router_id": request.POST.get("router_id"),
    }
    data ={
        "router": {
            "external_gateway_info": {}
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/routers/%(router_id)s' % {
            "router_id": req_params.get("router_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)

def v2_listNetworksFloatingips(request):
    """ Lists floating IPs that are accessible to the tenant who submits the request.
            Method:GET
            URI:/v2.0/floatingips
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
        'port': 9696,
        'uri': '/v2.0/floatingips'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksFloatingips(request):
    """ Creates a floating IP, and, if you specify port information,associates the floating IP with an internal port.
            Method:POST
            URI:/v2.0/floatingips
    """
    data = {
        "floatingip": {
            "floating_network_id": "a9e3c233-1b50-432b-838d-d0d35001bec8",
            "port_id": "07b4e5a5-d4ea-4e10-bb8b-d1ac604a22c0"
        }
    }
    token_id = '86e3aa60bea94771be8d3873677ae3bf'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/floatingips'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksFloatingips(request):
    """ Shows details for a specified floating IP.
            Method:GET
            URI:/v2.0/floatingips/{floatingip_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "floatingip_id" : request.GET.get("floatingip_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/floatingips/%(floatingip_id)s' % {
            "floatingip_id": req_params.get("floatingip_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksFloatingips(request):
    """ Updates a floating IP and its association with an internal port.
        Method:PUT
        URI:/v2.0/floatingips/{floatingip_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "floatingip_id" : request.GET.get("floatingip_id"),
        "port_id": request.GET.get("port_id"),
    }

    data = {
        "floatingip": {
            "port_id": req_params.get("port_id")
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
        "Accept: application/json"
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/floatingips/%(floatingip_id)s' % {
            "floatingip_id": req_params.get("floatingip_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteNetworksFloatingips(request):
    """ Deletes a floating IP and, if present, its associated port.
            Method:DELETE
            URI:/v2.0/floatingips/{floatingip_id}
    """
    token_id = '86e3aa60bea94771be8d3873677ae3bf'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/floatingips/%(floatingip_id)s' % {
            "floatingip_id": "99de7ead-9b10-4ce5-8af3-3b310824d59e"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listNetworksLoadbalancersVips(request):
    """ Lists VIPs.
            Method:GET
            URI:/v2.0/lb/vips
    """
    token_id = '9a07c577d19f47388a56c855e7902a77'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/vips'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksLoadbalancersVips(request):
    """ Creates a load balancer VIP.
            Method:POST
            URI:/v2.0/lb/vips
    """
    data = {
        "vip": {
            "protocol": "HTTP",
            "name": "NewVip",
            "admin_state_up": True,
            "subnet_id": "1bb4f79f-f240-46ff-a86e-a2ca3c6926e2",
            "pool_id": "61b1f87a-7a21-4ad3-9dda-7f81d249944f",
            "protocol_port": "80"
        }
    }
    token_id = '86e3aa60bea94771be8d3873677ae3bf'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/vips'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_detailNetworksLoadbalancersVips(request):
    """ Shows details for a specified VIP.
            Method:GET
            URI:/v2.0/lb/vips/{vip_id}
    """
    token_id = '86e3aa60bea94771be8d3873677ae3bf'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/vips/%(vip_id)s' % {
            "vip_id": "08527f24-6db2-4809-af16-332e2db49eda"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksLoadbalancersVips(request):
    """ Updates a specified load balancer VIP.
            Method:PUT
            URI:/v2.0/lb/vips/{vip_id}
    """
    data = {
        "vip": {
            "connection_limit": "1000"
        }
    }
    token_id = '86e3aa60bea94771be8d3873677ae3bf'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/vips/%(vip_id)s' % {
            "vip_id": "08527f24-6db2-4809-af16-332e2db49eda"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteNetworksLoadbalancersVips(request):
    """ Deletes a specified load balancer VIP.
            Method:DELETE
            URI:/v2.0/lb/vips/{vip_id}
    """
    token_id = '86e3aa60bea94771be8d3873677ae3bf'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/vips/%(vip_id)s' % {
            "vip_id": "08527f24-6db2-4809-af16-332e2db49eda"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listNetworksLoadbalancersHealthmonitors(request):
    """ Lists health monitors.
            Method:GET
            URI:/v2.0/lb/healthmonitors
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/healthmonitors'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksLoadbalancersHealthmonitors(request):
    """ Creates a load balancer health monitor.
            Method:POST
            URI:/v2.0/lb/healthmonitors
    """
    pass


def v2_detailNetworksLoadbalancersHealthmonitors(request):
    """ Shows details for a specified health monitor.
            Method:GET
            URI:/v2.0/lb/healthmonitors/{health_monitor_id}
    """
    pass


def v2_updateNetworksLoadbalancersHealthmonitors(request):
    """ Updates a specified load balancer health monitor.
            Method:PUT
            URI:/v2.0/lb/healthmonitors/{health_monitor_id}
    """
    pass


def v2_deleteNetworksLoadbalancersHealthmonitors(request):
    """ Deletes a specified load balancer health monitor.
            Method:DELETE
            URI:/v2.0/lb/healthmonitors/{health_monitor_id}
    """
    pass


def v2_listNetworksLoadbalancersPools(request):
    """ Lists pools.
            Method:GET
            URI:/v2.0/lb/pools
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/pools'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksLoadbalancersPools(request):
    """ Creates a load balancer pool.
            Method:POST
            URI:/v2.0/lb/pools
    """
    data = {
        "pool": {
            "admin_state_up": true,
            "description": "simple pool",
            "lb_algorithm": "ROUND_ROBIN",
            "listener_id": "39de4d56-d663-46e5-85a1-5b9d5fa17829",
            "name": "pool1",
                    "protocol": "HTTP",
                    "session_persistence": {
                            "cookie_name": "my_cookie",
                            "type": "APP_COOKIE"
                    }
        }
    }
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/pools'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_detailNetworksLoadbalancersPools(request):
    """ Shows details for a specified pool.
            Method:GET
            URI:/v2.0/lb/pools/{pool_id}
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/pools/%(pool_id)s' % {
            "pool_id": "01f42b4a-9fb9-46c9-8570-e2a400b9e325"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksLoadbalancersPools(request):
    """ Updates a specified load balancer pool.
            Method:PUT
            URI:/v2.0/lb/pools/{pool_id}
    """
    data = {
        "pool": {
            "name": "SuperPool"
        }
    }
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/pools/%(pool_id)s' % {
            "pool_id": "01f42b4a-9fb9-46c9-8570-e2a400b9e325"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteNetworksLoadbalancersPools(request):
    """ Deletes a specified load balancer pool.
            Method:DELETE
            URI:/v2.0/lb/pools/{pool_id}
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/pools/%(pool_id)s' % {
            "pool_id": "01f42b4a-9fb9-46c9-8570-e2a400b9e325"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_associatesNetworksLoadbalancersPoolsHealthmonitors(request):
    """ Associates a health monitor with a specified pool.
            Method:POST
            URI:/v2.0/lb/pools/{pool_id}/health_monitors
    """
    pass


def v2_disassociatesNetworksLoadbalancersPoolsHealthmonitors(request):
    """ Disassociates a specified health monitor from a pool.
            Method:DELETE
            URI:/v2.0/lb/pools/{pool_id}/health_monitors/{health_monitor_id}
    """
    pass


def v2_listNetworksLoadbalancersMemters(request):
    """ Lists members.
            Method:GET
            URI:/v2.0/lb/members
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/members'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksLoadbalancersMemters(request):
    """ Creates a load balancer member.
            Method:POST
            URI:/v2.0/lb/members
    """
    data = {
        "member": {
            "address": "10.0.0.8",
            "admin_state_up": True,
            "protocol_port": "80",
            "subnet_id": "552e7d57-2a89-4580-8597-f9142e6f875b",
            "weight": "1"
        }
    }
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/members'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_detailNetworksLoadbalancersMemters(request):
    """ Shows details for a specified member.
            Method:GET
            URI:/v2.0/lb/members/{member_id}
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/members/%(member_id)s' % {
            "member_id": "0e17f8da-e966-483d-b327-175c7b0ad81c"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksLoadbalancersMemters(request):
    """ Updates a specified load balancer member.
            Method:PUT
            URI:/v2.0/lb/members/{member_id}
    """
    data = {
        "member": {
            "admin_state_up": False
        }
    }
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/members/%(member_id)s' % {
            "member_id": "0e17f8da-e966-483d-b327-175c7b0ad81c"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteNetworksLoadbalancersMemters(request):
    """ Deletes a specified load balancer member.
            Method:DELETE
            URI:/v2.0/lb/members/{member_id}
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lb/members/%(member_id)s' % {
            "member_id": "0e17f8da-e966-483d-b327-175c7b0ad81c"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listNetworksLbaasLoadbalancers(request):
    """ Lists load balancers.
            Method:GET
            URI:/v2.0/lbaas/loadbalancers
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lbaas/loadbalancers'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksLbaasLoadbalancers(request):
    """ Creates a load balancer.
            Method:POST
            URI:/v2.0/lbaas/loadbalancers
    """
    pass


def v2_detailNetworksLbaasLoadbalancers(request):
    """ Shows details for a specified load balancer.
            Method:GET
            URI:/v2.0/lbaas/loadbalancers/{loadbalancer_id}
    """
    pass


def v2_updateNetworksLbaasLoadbalancers(request):
    """ Updates a specified load balancer.
            Method:PUT
            URI:/v2.0/lbaas/loadbalancers/{loadbalancer_id}
    """
    pass


def v2_removeNetworksLbaasLoadbalancers(request):
    """ Removes a specified load balancer.
            Method:DELETE
            URI:/v2.0/lbaas/loadbalancers/{loadbalancer_id}
    """
    pass


def v2_listNetworksLbaasListeners(request):
    """ Lists listeners.
            Method:GET
            URI:/v2.0/lbaas/listeners
    """
    token_id = '985f3f9fe96f48f4975f58187996432a'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lbaas/listeners'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksLbaasListeners(request):
    """ Creates a listener.
            Method:POST
            URI:/v2.0/lbaas/listeners
    """
    pass


def v2_detailNetworksLbaasListeners(request):
    """ Shows details for a specified listener.
            Method:GET
            URI:/v2.0/lbaas/listeners/{listener_id}
    """
    pass


def v2_updateNetworksLbaasListeners(request):
    """ Updates a specified listener.
            Method:PUT
            URI:/v2.0/lbaas/listeners/{listener_id}
    """
    pass


def v2_removeNetworksLbaasListeners(request):
    """ Removes a specified listener.
            Method:DELETE
            URI:/v2.0/lbaas/listeners/{listener_id}
    """
    pass


def v2_listNetworksLbaasPools(request):
    """ Lists pools.
            Method:GET
            URI:/v2.0/lbaas/pools
    """
    token_id = '5451f9ed4633436ba41c3e58d273e587'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/lbaas/pools'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksLbaasPools(request):
    """ Creates a pool.
            Method:POST
            URI:/v2.0/lbaas/pools
    """
    pass


def v2_detailNetworksLbaasPools(request):
    """ Shows details for a specified pool.
            Method:GET
            URI:/v2.0/lbaas/pools/{pool_id}
    """
    pass


def v2_updateNetworksLbaasPools(request):
    """ Updates a specified pool.
            Method:PUT
            URI:/v2.0/lbaas/pools/{pool_id}
    """
    pass


def v2_removeNetworksLbaasPools(request):
    """ Removes a specified pool.
            Method:DELETE
            URI:/v2.0/lbaas/pools/{pool_id}
    """
    pass


def v2_listNetworksLbaasPoolsMemters(request):
    """ Lists members of a specified pool.
            Method:GET
            URI:/v2.0/lbaas/pools/{pool_id}/members
    """
    pass


def v2_addNetworksLbaasPoolsMemters(request):
    """ Adds a member to a pool.
            Method:POST
            URI:/v2.0/lbaas/pools/{pool_id}/members
    """
    pass


def v2_detailNetworksLbaasPoolsMemters(request):
    """ Shows details for a specified pool member.
            Method:GET
            URI:/v2.0/lbaas/pools/{pool_id}/members/{member_id}
    """
    pass


def v2_updateNetworksLbaasPoolsMemters(request):
    """ Updates a specified member of a pool.
            Method:PUT
            URI:/v2.0/lbaas/pools/{pool_id}/members/{member_id}
    """
    pass


def v2_removeNetworksLbaasPoolsMemters(request):
    """ Removes a member from a pool.
            Method:DELETE
            URI:/v2.0/lbaas/pools/{pool_id}/members/{member_id}
    """
    pass


def v2_listNetworksLbaasHealthmonitors(request):
    """ Lists health monitors.
            Method:GET
            URI:/v2.0/lbaas/healthmonitors
    """
    pass


def v2_createNetworksLbaasHealthmonitors(request):
    """ Creates a health monitor.
            Method:POST
            URI:/v2.0/lbaas/healthmonitors
    """
    pass


def v2_detailNetworksLbaasHealthmonitors(request):
    """ Shows details for a specified health monitor.
            Method:GET
            URI:/v2.0/lbaas/healthmonitors/{health_monitor_id}
    """
    pass


def v2_updateNetworksLbaasHealthmonitors(request):
    """ Updates a specified health monitor.
            Method:PUT
            URI:/v2.0/lbaas/healthmonitors/{health_monitor_id}
    """
    pass


def v2_removeNetworksLbaasHealthmonitors(request):
    """ Removes a specified health monitor.
            Method:DELETE
            URI:/v2.0/lbaas/healthmonitors/{health_monitor_id}
    """
    pass


def v2_listNetworksVpnsVpnservices(request):
    """ Lists VPN services.
            Method:GET
            URI:/v2.0/vpn/vpnservices
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/vpnservices'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksVpnsVpnservices(request):
    """ Creates a VPN service.
        Method:POST
        URI:/v2.0/vpn/vpnservices
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "subnet_id": request.POST.get("subnet_id"),
        "router_id": request.POST.get("router_id"),
        "vpn_service_name": request.POST.get("vpn_service_name"),
    }
    data = {
        "vpnservice": {
            "subnet_id": req_params.get('subnet_id'),
            "router_id": req_params.get('router_id'),
            "name": req_params.get('vpn_service_name'),
            "admin_state_up": True
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/vpnservices'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_detailNetworksVpnsVpnservices(request):
    """ Shows details for a specified VPN service.
            Method:GET
            URI:/v2.0/vpn/vpnservices/{service_id}
    """
    token_id = '5451f9ed4633436ba41c3e58d273e587'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/vpn/vpnservices/%(service_id)s' % {
            "service_id": "8aacebcc-f945-4a5e-9089-091dfcfb54be"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksVpnsVpnservices(request):
    """ Updates a specified VPN service.
            Method:PUT
            URI:/v2.0/vpn/vpnservices/{service_id}
    """
    data = {
        "vpnservice": {
            "description": "Updated description"
        }
    }
    token_id = '5451f9ed4633436ba41c3e58d273e587'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/vpn/vpnservices/%(service_id)s' % {
            "service_id": "0f271d77-46cd-44b8-b848-808c8c1e9010"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_removeNetworksVpnsVpnservices(request):
    """ Removes a specified VPN service.
            Method:DELETE
            URI:/v2.0/vpn/vpnservices/{service_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "service_id": request.POST.get("service_id"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/vpnservices/%(service_id)s' % {
            "service_id": req_params.get('service_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listNetworksVpnsIkepolicies(request):
    """ Lists IKE policies.
            Method:GET
            URI:/v2.0/vpn/ikepolicies
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ikepolicies'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksVpnsIkepolicies(request):
    """ Creates an IKE policy.
            Method:POST
            URI:/v2.0/vpn/ikepolicies
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ikepolicy_name": request.POST.get('ikepolicy_name')
    }
    
    data = {
        "ikepolicy": {
            "phase1_negotiation_mode": "main",
            "auth_algorithm": "sha1",
            "encryption_algorithm": "aes-128",
            "pfs": "group5",
            "lifetime": {
                "units": "seconds",
                "value": 7200
            },
            "ike_version": "v1",
            "name": req_params.get('ikepolicy_name')
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ikepolicies'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksVpnsIkepolicies(request):
    """ Shows details for a specified IKE policy.
            Method:GET
            URI:/v2.0/vpn/ikepolicies/{ikepolicy_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ikepolicy_id": request.POST.get('ikepolicy_id')
    }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id')
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ikepolicies/%(ikepolicy_id)s' % {
            "ikepolicy_id": req_params.get('ikepolicy_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksVpnsIkepolicies(request):
    """ Updates policy settings in a specified IKE policy.
            Method:PUT
            URI:/v2.0/vpn/ikepolicies/{ikepolicy_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ikepolicy_id": request.POST.get('ikepolicy_id')
    }

    data = {
        "ikepolicy": {
            "encryption_algorithm": "aes-256"
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ikepolicies/%(ikepolicy_id)s' % {
            "ikepolicy_id": req_params.get('ikepolicy_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_removeNetworksVpnsIkepolicies(request):
    """ Removes a specified IKE policy.
            Method:DELETE
            URI:/v2.0/vpn/ikepolicies/{ikepolicy_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ikepolicy_id": request.POST.get("ikepolicy_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ikepolicies/%(ikepolicy_id)s' % {
            "ikepolicy_id": req_params.get('ikepolicy_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listNetworksVpnsIpsecpolicies(request):
    """ Lists IPSec policies.
        Method:GET
        URI:/v2.0/vpn/ipsecpolicies
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsecpolicies'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksVpnsIpsecpolicies(request):
    """ Creates an IPSec policy.
        Method:POST
        URI:/v2.0/vpn/ipsecpolicies
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ipsecpolicie_name": request.POST.get('ipsecpolicie_name')
    }
    data = {
        "ipsecpolicy": {
            "name": req_params.get('ipsecpolicie_name'),
            "transform_protocol": "esp",
            "auth_algorithm": "sha1",
            "encapsulation_mode": "tunnel",
            "encryption_algorithm": "aes-128",
            "pfs": "group5",
            "lifetime": {
                "units": "seconds",
                "value": 7200
            }
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsecpolicies'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksVpnsIpsecpolicies(request):
    """ Shows details for a specified IPSec policy.
            Method:GET
            URI:/v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ipsecpolicy_id":request.POST.get('ipsecpolicy_id')
    }

    head = [
        "X-Auth-Token: %s" % request.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsecpolicies/%(ipsecpolicy_id)s' % {
            "ipsecpolicy_id": req_params.get('ipsecpolicy_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksVpnsIpsecpolicies(request):
    """ Updates policy settings in a specified IPSec policy.
            Method:PUT
            URI:/v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ipsecpolicy_id":request.POST.get('ipsecpolicy_id')
    }
    data = {
        "ipsecpolicy": {
            "pfs": "group14"
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsecpolicies/%(ipsecpolicy_id)s' % {
            "ipsecpolicy_id": req_params.get('ipsecpolicy_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_removeNetworksVpnsIpsecpolicies(request):
    """ Removes a specified IPSec policy.
            Method:DELETE
            URI:/v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ipsecpolicy_id": request.POST.get("ipsecpolicy_id"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsecpolicies/%(ipsecpolicy_id)s' % {
            "ipsecpolicy_id": req_params.get('ipsecpolicy_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listNetworksVpnsIpsecsiteconnections(request):
    """ Lists IPSec connections.
        Method:GET
        URI:/v2.0/vpn/ipsec-site-connections
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsec-site-connections'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksVpnsIpsecsiteconnections(request):
    """ Creates an IPSec connection.
        Method:POST
        URI:/v2.0/vpn/ipsec-site-connections
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ipsecpolicy_id": request.POST.get("ipsecpolicy_id"),
        "ikepolicy_id": request.POST.get("ikepolicy_id"),
        "ipsecpolicy_id": request.POST.get("ipsecpolicy_id"),
        "vpnservice_id": request.POST.get("vpnservice_id"),
        "peer_ep_group_id": request.POST.get("peer_ep_group_id"),
        "local_ep_group_id": request.POST.get("local_ep_group_id"),
        "peer_address": request.POST.get("peer_address"),
        "peer_id": request.POST.get("peer_id"),
        "ipsec_site_connection_name": request.POST.get("ipsec_site_connection_name"),
    }

    data = {
        "ipsec_site_connection": {
            "psk": "secret",
            "initiator": "bi-directional",
            "ipsecpolicy_id": req_params.get('ipsecpolicy_id'),
            "admin_state_up": true,
            "mtu": "1500",
            "peer_ep_group_id": req_params.get('peer_ep_group_id'),
            "ikepolicy_id": req_params.get('ikepolicy_id'),
            "vpnservice_id": req_params.get('vpnservice_id'),
            "local_ep_group_id": req_params.get('local_ep_group_id'),
            "peer_address": req_params.get('peer_address'),
            "peer_id": req_params.get('peer_id'),
            "name": req_params.get('ipsec_site_connection_name')
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsec-site-connections'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksVpnsIpsecsiteconnections(request):
    """Shows details for a specified IPSec connection.
        Method:GET
        URI:/v2.0/vpn/ipsec-site-connections/{connection_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ipsec_site_connection_id": request.POST.get('ipsec_site_connection_id')
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsec-site-connections/%s' % req_params.get('ipsec_site_connection_id')
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateNetworksVpnsIpsecsiteconnections(request):
    """ Updates connection settings for a specified IPSec connection.
            Method:PUT
            URI:/v2.0/vpn/ipsec-site-connections/{connection_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ipsec_site_connection_id": request.POST.get('ipsec_site_connection_id')
        
    }
    data = {
        "ipsec_site_connection": {
            "mtu": "2000"
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsec-site-connections/%(ipsec_site_connection_id)s' % {
            "ipsec_site_connection_id":req_params.get('ipsec_site_connection_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)

def v2_removeNetworksVpnsIpsecsiteconnections(request):
    """ Removes a specified IPSec connection.
            Method:DELETE
            URI:/v2.0/vpn/ipsec-site-connections/{connection_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "ipsec_site_connection_id": request.POST.get('ipsec_site_connection_id')
        
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('token_id'),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 9696,
        'uri': '/v2.0/vpn/ipsec-site-connections/%s' % req_params.get('ipsec_site_connection_id')
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)

def v2_listNetworksMultipleIncludeSegments(request):
    """ Lists networks that are accessible to the tenant who submits the request.
            Networks with multiple segments include the segments list in the response.
            Method:GET
            URI:/v2.0/networks
    """
    token_id = '5451f9ed4633436ba41c3e58d273e587'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/networks'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createNetworksMultipleIncludeSegments(request):
    """ Creates a network with multiple segment mappings.
            Method:POST
            URI:/v2.0/networks
    """
    data = {
        "network": {
            "segments": [
                {
                    "provider:segmentation_id": "2",
                    "provider:physical_network": "8bab8453-1bc9-45af-8c70-f83aa9b50453",
                    "provider:network_type": "vlan"
                },
                {
                    "provider:physical_network": "8bab8453-1bc9-45af-8c70-f83aa9b50453",
                    "provider:network_type": "stt"
                }
            ],
            "name": "nets000000000000000000000000001111111111111",
            "admin_state_up": True
        }
    }
    token_id = '5451f9ed4633436ba41c3e58d273e587'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 9696,
        'uri': '/v2.0/networks'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showNetworksMultipleIncludeSegments(request):
    """ Shows details for a specified network with multiple segments.
            Method:GET
            URI:/v2.0/networks/{network_id}
    """
    pass
