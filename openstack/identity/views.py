from __future__ import unicode_literals
from django.http import HttpResponse

from openstack.utils import HandlePycurl

import json

########################################################
#                       V2
########################################################


def v2_obtainToken(request):
    """ Authenticates and generates a token. 
            uri: POST /v2.0/tokens
    """
    req_params = {
        "remotehost": request.POST.get('remotehost'),
        "tenantName": request.POST.get('tenantName'),
        "username": request.POST.get("username"),
        "password": request.POST.get('password')

    }
    data = {
        "auth": {
            "tenantName": req_params.get("tenantName"),
            "passwordCredentials": {
                "username": req_params.get("username"),
                "password": req_params.get("password")
            }
        }
    }
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v2.0/tokens'
    }
    head = [
        "Content-Type: application/json",
        "Accept: application/json"
    ]

    # print request.__class__.__bases__
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head=head)

    return HttpResponse(context)


def v2_listTokenTenants(request):
    """ Lists tenants to which the specified token has access.
            uri: GET  /v2.0/tenants
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
        "Content-Type: application/json",
        "Accept: application/json"
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v2.0/tenants'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_validateToken(request):
    """ Validates a token and confirms that it belongs to a specified tenant.
            Method:GET
            URI:/v2.0/tokens/{tokenId}{?belongsTo}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
        "Content-Type: application/json",
        "Accept: application/json"
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8774,
        'uri': '/v2.0/tokens/%(tokenId)s' % {
            "tokenId": req_params.get("token_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head=[])
    return HttpResponse(context)


def v2_listUsers(request):
    """ Lists users.
            Method:GET
            URI:/v2.0/users{?limit,marker}
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
        'port': 35357,
        'uri': '/v2.0/users'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_addUser(request):
    """ Adds a user.
            Method:POST
            URI:/v2.0/users
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "userId": request.POST.get("userId"),
        "userName": request.POST.get("userName"),
        "userEmail": request.POST.get("userEmail")
    }
    data = {
        "user": {
            "id": req_params.get("userId"),
            "name": req_params.get("userName"),
            "email": req_params.get("userEmail"),
            "enabled": True
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/users'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_detailByNameUser(request):
    """ Gets detailed information about a specified user by user name.
            Method:GET
            URI:/v2.0/users{?name}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "userName": request.GET.get("userName"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/users?name=%(userName)s' % {
            "userName": req_params.get("userName")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailByIdUser(request):
    """ Gets detailed information about a specified user by user ID.
            Method:GET
            URI:/v2.0/users/{user_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "userId": request.GET.get("userId"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/users/%(userId)s' % {
            "userId": req_params.get("userId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateUser(request):
    """ Updates a user.
            Method:PUT
            URI:/v2.0/users/{userId}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "userId": request.POST.get("userId"),
        "userName": request.POST.get("userName"),
        "userEmail": request.POST.get("userEmail")
    }
    data = {
        "user": {
            # "id": "u1000", # no change user id
            "name": req_params.get("userName"),
            "email": req_params.get("userEmail"),
            "enabled": True
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/users/%(userId)s' % {
            "userId": req_params.get("userId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteUser(request):
    """ Deletes a user.
            Method:DELETE
            URI:/v2.0/users/{userId}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "userId": request.POST.get("userId")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/users/%(userId)s' % {
            "userId": req_params.get("userId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete seccussful")


def v2_listUserGlobalRole(request):
    """ Lists global roles for a specified user.
            Method:GET
            URI:/v2.0/users/{userId}/roles{?serviceId,limit,marker}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "user_id": request.GET.get("user_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/users/%(userId)s/roles' % {
            "userId": req_params.get("user_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_addGlobalRoleToUser(request):
    """ Adds a specific global role to a user.
            Method:PUT
            URI:/v2.0/users/{userId}/roles/OS-KSADM/{roleId}
    """
    pass


def v2_deleteGlobalRoleFromUser(request):
    """ Deletes a specific global role from a user.
            Method:DELETE
            URI:/v2.0/users/{userId}/roles/OS-KSADM/{roleId}
    """
    pass


def v2_listTenant(request):
    """ Lists all tenants.
            Method:GET
            URI:/v2.0/tenants{?limit,marker}
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
        'port': 35357,
        'uri': '/v2.0/tenants'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailByNameTenant(request):
    """ Gets detailed information about a specified tenant by name.
            Method:GET
            URI:/v2.0/tenants{?name}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenantName": request.GET.get("tenantName")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/tenants?name=%(name)s' % {
            "name": req_params.get("tenantName")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailByIdTenant(request):
    """ Gets detailed information about a specified tenant by ID.
            Method:GET
            URI:/v2.0/tenants/{tenantId}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenantId": request.GET.get("tenantId")
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/tenants/%(tenantId)s' % {
            "tenantId": req_params.get("tenantId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listTenantUserRoles(request):
    """ Lists roles for a specified user on a specified tenant. Excludes global roles.
            Method:GET
            URI:/v2.0/tenants/{tenantId}/users/{userId}/roles{?limit,marker}
    """

    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenantId": request.GET.get("tenantId"),
        "userId": request.GET.get("userId"),
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/tenants/%(tenantId)s/users/%(userId)s/roles' % {
            "tenantId": req_params.get("tenantId"),
            "userId": req_params.get("userId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createTenant(request):
    """ Creates a tenant.
            Method:POST
            URI:/v2.0/tenants
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenantName": request.POST.get("tenantName"),
        "description": request.POST.get("description", "description tenant")
    }

    data = {
        "tenant": {
            "name": req_params.get("tenantName"),
            "description": req_params.get("description"),
            "enabled": True
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/tenants'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_updateTenant(request):
    """ Updates a tenant.
            Method:POST
            URI:/v2.0/tenants/{tenantId}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenantId": request.POST.get("tenantId")    ,
        "tenantName": request.POST.get("tenantName"),
        "description": request.POST.get("description")
    }
    data = {
        "tenant": {
            "id": req_params.get("tenantId"),
            "name": req_params.get("tenantName"),
            "description": req_params.get("description"),
            "enabled": True
        }
    }
    token_id = 'ce894ef7c23d462fab19d8ace0b34e73'

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/tenants/%(tenantId)s' % {
            "tenantId": req_params.get("tenantId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteTenant(request):
    """ Deletes a tenant.
            Method:DELETE
            URI:/v2.0/tenants/{tenantId}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenantId": request.GET.get("tenantId") ,
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/tenants/%(tenantId)s' % {
            "tenantId": req_params.get("tenantId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete seccussful")


def v2_listTenantUser(request):
    """ Lists all users for a tenant.
            Method: GET
            URI:/v2.0/tenants/{tenantId}/users{?limit,marker}
    """
    token_id = 'ce894ef7c23d462fab19d8ace0b34e73'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 35357,
        'uri': '/v2.0/tenants/%(tenantId)s/users' % {
            "tenantId": "6929b9cbbd914699915ca8be4c283240"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_addTenantUserRole(request):
    """ Adds a specified role to a user for a tenant.
            Method:PUT
            URI:/v2.0/tenants/{tenantId}/users/{userId}/roles/OS-KSADM/{roleId}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenantId": request.POST.get("tenantId")    ,
        "userId": request.POST.get("userId"),
        "roleId": request.POST.get("roleId"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/tenants/%(tenantId)s/users/%(userId)s/roles/OS-KSADM/%(roleId)s' % {
            "tenantId": req_params.get("tenantId"),
            "userId": req_params.get("userId"),
            "roleId": req_params.get("roleId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, head=head)
    return HttpResponse(context)


def v2_deleteTenantRoleFromUser(request):
    """ Deletes a specified role from a user on a tenant.
            Method:DELETE
            URI:/v2.0/tenants/{tenantId}/users/{userId}/roles/OS-KSADM/{roleId}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenantId": request.POST.get("tenantId")    ,
        "userId": request.POST.get("userId"),
        "roleId": request.POST.get("roleId"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/tenants/%(tenantId)s/users/%(userId)s/roles/OS-KSADM/%(roleId)s' % {
            "tenantId": req_params.get("tenantId"),
            "userId": req_params.get("userId"),
            "roleId": req_params.get("roleId")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")


def v2_infoRoleByName(request):
    """ Gets a role by name.
            Method:GET
            URI:/v2.0/OS-KSADM/roles
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenantId": request.GET.get("tenantId") ,
        "userId": request.GET.get("userId"),
        "roleId": request.GET.get("roleId"),
    }
    token_id = 'ce894ef7c23d462fab19d8ace0b34e73'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/roles'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_listRoles(request):
    """ Lists roles.
            Method:GET
            URI:/v2.0/OS-KSADM/roles/{?limit,marker}
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
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/roles/'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_addRole(request):
    """ Adds a role.
            Method:POST
            URI:/v2.0/OS-KSADM/roles
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "role_id": request.POST.get("role_id"),
        "role_name": request.POST.get("role_name"),
        "role_description": request.POST.get("role_description")
    }

    data = {
        "role": {
            "id": req_params.get("role_id"),
            "name": req_params.get("role_name"),
            "description": req_params.get("role_description")
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/roles'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_infoRoleById(request):
    """ Gets information for a specified role.
            Method:GET
            URI:/v2.0/OS-KSADM/roles/{roleId}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "role_id": request.GET.get("role_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/roles/%(roleId)s' % {
            "roleId": req_params.get("role_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deleteRole(request):
    """ Deletes a role.
            Method:DELETE
            URI:/v2.0/OS-KSADM/roles/{roleId}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "role_id": request.POST.get("role_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/roles/%(roleId)s' % {
            "roleId": req_params.get("role_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or "delete successfully")


def v2_listServices(request):
    """ Lists services.
            Method:GET
            URI:/v2.0/OS-KSADM/services{?limit,marker}
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
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/services'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_addService(request):
    """ Adds a service.
            Method:POST
            URI:/v2.0/OS-KSADM/services
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "service_id": request.POST.get("service_id"),
        "service_name": request.POST.get("service_name"),
        "service_type": request.POST.get("service_type"),
        "service_desc": request.POST.get("service_desc"),
    }
    data = {
        "OS-KSADM:service": {
            "id": req_params.get("service_id"),
            "name": req_params.get("service_name"),
            "type": req_params.get("service_type"),
            "description": req_params.get("service_desc")
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/services'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_infoServiceByName(request):
    """ Gets a service by name.
            Method:GET
            URI:/v2.0/OS-KSADM/services/{?name}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "service_name": request.GET.get("service_name"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/services?name="%(name)s"' % {
            "name": req_params.get("service_name")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    print url
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_infoServiceById(request):
    """ Gets a service.
            Method:GET
            URI:/v2.0/OS-KSADM/services/{serviceId}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "service_id": request.GET.get("service_id"),
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/services/%(serviceId)s' % {
            "serviceId": req_params.get("service_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deleteService(request):
    """ Deletes a service.
            Method:DELETE
            URI:/v2.0/OS-KSADM/services/{serviceId}
    """
    token_id = 'ce894ef7c23d462fab19d8ace0b34e73'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 35357,
        'uri': '/v2.0/OS-KSADM/services/%(serviceId)s' % {
            "serviceId": "14634021651843109aa9342cc9c924f1"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


########################################################
#                       V3
########################################################
def v3_obtainAuthToken(request):
    """ Authenticates and generates a token.
            Method: POST
            URI:/v3/auth/tokens
    """
    req_params = {
        "remotehost": request.POST.get("remotehost"),
        "admin_name": request.POST.get("admin_name"),
        "admin_pwd": request.POST.get("admin_pwd"),
        "project_name": request.POST.get("project_name")
    }
    print req_params
    data = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": req_params.get("admin_name"),
                        "domain": {"id": "default"},
                        "password": req_params.get("admin_pwd")
                    }
                }
            },
            "scope": {
                "project": {
                    "name": req_params.get("project_name"),
                    "domain": {"id": "default"}
                }
            }
        }
    }

    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/auth/tokens'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, data=json.dumps(data), head=[], v3=True)

    return HttpResponse(context)


def v3_validateAuthToken(request):
    """ Validates a specified token.
            Method:GET
            URI:/v3/auth/tokens
    """
    req_params = {
        "remotehost": request.POST.get("remotehost"),
        "X-Auth-Token": request.POST.get('X-Auth-Token'),
        "X-Subject-Token": request.POST.get('X-Subject-Token')
    }
    head = [
        "X-Auth-Token: %s" % req_params.get('X-Auth-Token'),
        "X-Subject-Token: %s" % req_params.get('X-Subject-Token')
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 5000,
        'uri': '/v3/auth/tokens'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)

    return HttpResponse(context)


def v3_checkAuthToken(request):
    """ Validates a specified token.
            Method:HEAD
            URI:/v3/auth/tokens
    """
    pass


def v3_revokeAuthToken(request):
    """ Revokes a specified token.
            Method:DELETE
            URI:/v3/auth/tokens
    """
    pass


def v3_addUser(request):
    """ Adds a user.
            Method:POST
            URI:/v3/users
    """
    req_params = {
        "remotehost": request.POST.get("remotehost"),
        "token_id": request.POST.get("token_id"),
        "project_id": request.POST.get("project_id"),
        "desc": request.POST.get("desc"),
        "domain_id": request.POST.get("domain_id"),
        "user_email": request.POST.get("user_email"),
        "user_name": request.POST.get("user_name"),
        "user_pwd": request.POST.get("user_pwd")
    }
    data = {
        "user": {
            "default_project_id": req_params.get("project_id"),
            "description": req_params.get("desc"),
            "domain_id": req_params.get("domain_id"),
            "email": req_params.get("user_email"),
            "enabled": True,
            "name": req_params.get("user_name"),
            "password": req_params.get("user_pwd")
        }
    }

    head = [
        "Content-Type: application/json",
        "Accept: application/json",
        "X-Auth-Token: %s" % req_params.get("token_id")
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/users'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head=head)

    return HttpResponse(context)


def v3_listUsers(request):
    """ Lists users.
            Method:GET
            URI:/v3/users{?domain_id,name,enabled,page,per_page}
    """
    pass


def v3_updateUser(request):
    """ Updates the password for or enables or disables a specified userself.
            Method:PATCH
            URI:/v3/users/{user_id}
    """
    pass


def v3_deleteUser(request):
    """ Deletes a specified user
            Method:DELETE
            URI:/v3/users/{user_id}
    """
    pass


def v3_detailUser(request):
    """ Shows details for a specified user.
            Method:GET
            URI:/v3/users/{user_id}
    """
    pass


def v3_listUserGroup(request):
    """ Lists groups for a specified user.
            Method:GET
            URI:/v3/users/{user_id}/groups
    """
    pass


def v3_listUserProject(request):
    """ List projects for a specified user.
            Method:GET
            URI:/v3/users/{user_id}/projects
    """
    req_params = {
        "remotehost": request.GET.get("remotehost"),
        "token_id": request.GET.get("token_id"),
        "user_id": request.GET.get("user_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/users/%(user_id)s/projects' % {
            'user_id': req_params.get('user_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v3_addGroup(request):
    """ Adds a group.
            Method:POST
            URI:/v3/groups
    """
    pass


def v3_listGroups(request):
    """ Lists groups.
            Method:GET
            URI:/v3/groups{?domain_id,page,per_page}
    """
    pass


def v3_detailGroup(request):
    """ Shows details for a specified group.
            Method":GET
            URI:/v3/groups/{group_id}
    """
    pass


def v3_updateGroup(request):
    """ Updates a specified group.
            Method:PATCH
            URI:/v3/groups/{group_id}
    """
    pass


def v3_deleteGroup(request):
    """ Deletes a specified group.
            Method:DELETE
            URI:/v3/groups/{group_id}
    """
    pass


def v3_listGroupUsers(request):
    """ Lists the users in a specified group.
            Method:GET
            URI:/v3/groups/{group_id}/users{?name, page,per_page,domain_id,description,name,enabled,page,per_page}
    """
    pass


def v3_addUserToGroup(request):
    """ Adds a user to a specified group.
            Method:PUT
            URI:/v3/groups/{group_id}/users/{user_id}
    """
    pass


def v3_removeUserFromGroup(request):
    """ Removes a user from a group.
            Method:DELETE
            URI:/v3/groups/{group_id}/users/{user_id}
    """
    pass


def v3_validateUserInGroup(request):
    """ Validates that a user is in a group.
            Method:HEAD
            URI:/v3/groups/{group_id}/users/{user_id}
    """
    pass


def v3_addCredential(request):
    """ Adds a credential.
            Method:POST
            URI:/v3/credentials
    """
    pass


def v3_listCredentials(request):
    """ Lists credentials.
            Method:GET
            URI:/v3/credentials{?page,per_page}
    """
    pass


def v3_detailCredential(request):
    """ Shows details for a specified credential.
            Method:GET
            URI:/v3/credentials/{credential_id}
    """
    pass


def v3_updateCredential(request):
    """ Updates a specified credential.
            Method:PATCH
            URI:/v3/credentials/{credential_id}
    """
    pass


def v3_deleteCredential(request):
    """ Deletes a specified credential.
            Method:DELETE
            URI:/v3/credentials/{credential_id}
    """
    pass


def v3_addRole(request):
    """ Adds a role.
            Method:POST
            URI:/v3/roles
    """
    pass


def v3_listRoles(request):
    """ Lists roles.
            Method:GET
            URI:/v3/roles{?name,page,per_page}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "name": request.GET.get('role_name')
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    if req_params.get('name') == '':  # and '' or '?name=%s' % req_params.get('name')
        role_name = ''
    else:
        role_name = '?name=%s' % req_params.get('name')
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v3/roles%s' % role_name  # ?name=_member_
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v3_detailRoles(request):
    """Shows details for a role.
       Method: GET
       URI: /v3/roles/{role_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "role_id": request.GET.get('role_id')
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v3/roles/%(role_id)s' % {
            'role_id': req_params.get('role_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v3_addPolicies(request):
    """ Adds a policy.
            Method:POST
            URI:/v3/policies
    """
    pass


def v3_listPolicies(request):
    """ Lists policies.
            Method:GET
            URI:/v3/policies{?type,page,per_page}
    """
    pass


def v3_updatePolicies(request):
    """ Updates a specified policy.
            Method:PATCH
            URI:/v3/policies/{policy_id}
    """
    pass


def v3_detailPolicie(request):
    """ Shows details for a specified policy.
            Method:GET
            URI:/v3/policies/{policy_id}
    """
    pass


def v3_deletePolicie(request):
    """ Deletes a specified policy.
            Method:DELETE
            URI:/v3/policies/{policy_id}
    """
    pass


def v3_addDomain(request):
    """ Adds a domain.
            Method:POST
            URI:/v3/domains
    """
    req_params = {
        "remotehost": request.POST.get("remotehost"),
        "token_id": request.POST.get("token_id"),
        "domain_name": request.POST.get("domain_name"),
        "domain_desc": request.POST.get("domain_desc"),
    }
    data = {
        "domain": {
            "description": req_params.get("domain_desc"),
            "enabled": True,
            "name": req_params.get("domain_name")
        }
    }
    head = [
        "Content-Type: application/json",
        "Accept: application/json",
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v3/domains'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)

    return HttpResponse(context)


def v3_listDomains(request):
    """ Lists domains.
            Method:GET
            URI:/v3/domains{?name,enabled,page,per_page}
    """
    req_params = {
        "remotehost": request.GET.get("remotehost"),
        "token_id": request.GET.get("token_id"),
    }
    head = [
        "Content-Type: application/json",
        "Accept: application/json",
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 35357,
        'uri': '/v3/domains'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)

    return HttpResponse(context)


def v3_detailDomain(request):
    """ Shows details for a specified domain.
            Method:
            URI:/v3/domains/{domain_id}
    """
    pass


def v3_updateDomain(request):
    """ Updates a specified domain.
            Method:PATCH
            URI:/v3/domains/{domain_id}
    """
    pass


def v3_deleteDomain(request):
    """ Deletes a specified domain.
            Method:DELETE
            URI:/v3/domains/{domain_id}
    """
    pass


def v3_listDomainUserRoles(request):
    """ Lists roles for a user on a domain.
            Method:GET
            URI:/v3/domains/{domain_id}/users/{user_id}/roles
    """
    pass


def v3_grantDomainUserRoles(request):
    """ Grants a role to a specified domain user.
            Method:PUT
            URI:/v3/domains/{domain_id}/users/{user_id}/roles/{role_id}
    """
    pass


def v3_checkDomainUserRoles(request):
    """ Validates that a user has a role on a domain.
            Method:HEAD
            URI:/v3/domains/{domain_id}/users/{user_id}/roles/{role_id}
    """
    pass


def v3_revokeDomainUserRoles(request):
    """ Revokes a role from a specified domain user.
            Method:DELETE
            URI:/v3/domains/{domain_id}/users/{user_id}/roles/{role_id}
    """
    pass


def v3_listDomainGroupRoles(request):
    """ Lists roles for a specified domain group.
            Method:GET
            URI:/v3/domains/{domain_id}/groups/{group_id}/roles
    """
    pass


def v3_grantDomainGroupRoles(request):
    """ Grants a specified role to a specified domain group.
            Method:PUT
            URI:/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}
    """
    pass


def v3_checkDomainGroupRoles(request):
    """ Validates that a group has a role on a domain.
            Method:HEAD
            URI:/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}
    """
    pass


def v3_revokeDomainGroupRoles(request):
    """ Revokes a role from a group on a domain.
            Method:DELETE
            URI:/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}
    """
    pass


def v3_addEndpoint(request):
    """ Adds an endpoint.
            Method:POST
            URI:/v3/endpoints
    """
    pass


def v3_listEndpoints(request):
    """ Lists available endpoints.
            Method:GET
            URI:/v3/endpoints{?interface,service_id,page,per_page}
    """
    pass


def v3_updateEndpoint(request):
    """ Updates a specified endpoint.
            Method:PATCH
            URI:/v3/endpoints/{endpoint_id}
    """
    pass


def v3_deleteEndpoint(request):
    """ Deletes a specified endpoint.
            Method:DELETE
            URI:/v3/endpoints/{endpoint_id}
    """
    pass


def v3_addService(request):
    """ Adds a service.
            Method:POST
            URI:/v3/services
    """
    pass


def v3_listServices(request):
    """ Lists services.
            Method:GET
            URI:/v3/services{?type,page,per_page}
    """
    pass


def v3_detailService(request):
    """ Shows details for a specified service.
            Method:GET
            URI:/v3/services/{service_id}
    """
    pass


def v3_updateService(request):
    """ Updates a specified service.
            Method:PATCH
            URI:/v3/services/{service_id}
    """
    pass


def v3_deleteService(request):
    """ Deletes a specified service.
            Method:DELETE
            URI:/v3/services/{service_id}
    """
    pass


def v3_addProject(request):
    """ Adds a project.
            Method:POST
            URI:/v3/projects
    """
    req_params = {
        "remotehost": request.POST.get("remotehost"),
        "token_id": request.POST.get("token_id"),
        "pro_desc": request.POST.get("pro_desc"),
        "domain_id": request.POST.get("domain_id"),
        "pro_name": request.POST.get("pro_name"),
    }
    data = {
        "project": {
            "description": req_params.get("pro_desc"),
            "domain_id": req_params.get("domain_id"),
            "enabled": True,
            "name": req_params.get("pro_name")
        }
    }
    head = [
        "Content-Type: application/json",
        "Accept: application/json",
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/projects'
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)

    return HttpResponse(context)


def v3_listprojects(request):
    """ Lists projects.
            Method:GET
            URI:/v3/projects{?domain_id,name,enabled,page,per_page}
    """
    req_params = {
        "remotehost": request.GET.get("remotehost"),
        "token_id": request.GET.get("token_id"),
        "name": request.GET.get("role_name")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    if req_params.get('name') == '':  # and '' or '?name=%s' % req_params.get('name')
        role_name = ''
    else:
        role_name = '?name=%s' % req_params.get('name')
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/projects%s' % role_name
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    code, context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v3_detailProject(request):
    """ Shows details for a specified project.
            Method:GET
            URI:/v3/projects/{project_id}
    """
    req_params = {
        "remotehost": request.GET.get("remotehost"),
        "token_id": request.GET.get("token_id"),
        "project_id": request.GET.get("project_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]

    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/projects/%(project_id)s' % {
            'project_id': req_params.get('project_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    code, context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v3_updateProject(request):
    """ Updates a specified project.
            Method:PATCH
            URI:/v3/projects/{project_id}
    """
    pass


def v3_deleteProject(request):
    """ Deletes a specified project.
            Method:DELETE
            URI:/v3/projects/{project_id}
    """
    pass


def v3_grantProjectUserRole(request):
    """ Grants a role to a user on a project.
            Method:PUT
            URI:/v3/projects/{project_id}/users/{user_id}/roles/{role_id}
    """
    req_params = {
        "remotehost": request.POST.get("remotehost"),
        "token_id": request.POST.get("token_id"),
        "project_id": request.POST.get("project_id"),
        "user_id": request.POST.get("user_id"),
        "role_id": request.POST.get("role_id"),
    }
    data = dict()
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/projects/%(project_id)s/users/%(user_id)s/roles/%(role_id)s' % {
            "project_id": req_params.get('project_id'),
            "user_id": req_params.get('user_id'),
            "role_id": req_params.get('role_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v3_listProjectUserRole(request):
    """ Lists roles for a user in a project.
            Method:GET
            URI:/v3/projects/{project_id}/users/{user_id}/roles
    """
    req_params = {
        "remotehost": request.GET.get("remotehost"),
        "token_id": request.GET.get("token_id"),
        "project_id": request.GET.get("project_id"),
        "user_id": request.GET.get('user_id')
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]

    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/projects/%(project_id)s/users/%(user_id)s/roles' % {
            'project_id': req_params.get('project_id'),
            'user_id': req_params.get('user_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    code, context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v3_checkProjectUserRole(request):
    """ Validates that a user has a specified role on a project.
            Method:HEAD
            URI:/v3/projects/{project_id}/users/{user_id}/roles/{role_id}
    """
    pass


def v3_revokeProjectUserRole(request):
    """ Revokes a role from a project user.
            Method:DELETE
            URI:/v3/projects/{project_id}/users/{user_id}/roles/{role_id}
    """
    req_params = {
        "remotehost": request.POST.get("remotehost"),
        "token_id": request.POST.get("token_id"),
        "project_id": request.POST.get("project_id"),
        "user_id": request.POST.get("user_id"),
        "role_id": request.POST.get("role_id"),
    }
    data = dict()
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 5000,
        'uri': '/v3/projects/%(project_id)s/users/%(user_id)s/roles/%(role_id)s' % {
            "project_id": req_params.get('project_id'),
            "user_id": req_params.get('user_id'),
            "role_id": req_params.get('role_id')
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context or 'delete successfully')


def v3_listProjectGroupRole(request):
    """ Lists roles for a project group.
            Method:GET
            URI:/v3/projects/{project_id}/groups/{group_id}/roles
    """
    pass


def v3_grantProjectGroupRole(request):
    """ Grants a role to a project group.
            Method:PUT
            URI:/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}
    """
    pass


def v3_checkProjectGroupRole(request):
    """ Validates that a project group has a role.
            Method:HEAD
            URI:/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}
    """
    pass


def v3_revokeProjectGroupRole(request):
    """ Revokes a role from a project group.
            Method:DELETE
            URI:/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}
    """
