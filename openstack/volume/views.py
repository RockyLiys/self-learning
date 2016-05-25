from __future__ import unicode_literals
from django.http import HttpResponse

from openstack.utils import HandlePycurl

import json


def v2_listVolumesExtensions(request):
    """ Lists Block Storage API extensions.
        Method:GET
        URI:/v2/{tenant_id}/extensions
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/extensions' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createTenantVolumes(request):
    """ Creates a volume.
        Method:POST
        URI:/v2/{tenant_id}/volumes
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id"),
        "volume_name": request.POST.get("volume_name"),
        "volume_size": request.POST.get("volume_size")
    }
    data = {
        "volume": {
            "status": "creating",
            "description": req_params.get("volume_name"),
            "availability_zone": None,
            "source_volid": None,
            "consistencygroup_id": None,
            "snapshot_id": None,
            "source_replica": None,
            "size": req_params.get("volume_size"),
            "user_id": None,
            "name": req_params.get("volume_name"),
            "imageRef": None,
            "attach_status": "detached",
            "volume_type": None,
            "project_id": None,
            "os-volume-type-access: is_public": True,
            "metadata": {}
        }
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/volumes' % {
            "tenant_id": req_params.get("tenant_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_listTenantVolumes(request):
    """ Lists summary information for all Block Storage volumes that the tenant who submits the request can access.
        Method:GET
        URI:/v2/{tenant_id}/volumes{?sort,limit,marker}
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
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/volumes' % {
            "tenant_id": req_params.get("tenant_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailTenantVolumes(request):
    """ Lists detailed information for all Block Storage volumes that the tenant who submits the request can access.
        Method:GET
        URI:/v2/{tenant_id}/volumes/detail{?sort,limit,marker}
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
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/volumes/detail' % {
            "tenant_id": req_params.get("tenant_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_showTenantVolumes(request):
    """ Shows information about a specified volume.
        Method:GET
        URI:/v2/{tenant_id}/volumes/{volume_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "volume_id": request.GET.get("volume_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get('remotehost'),
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/volumes/%(volume_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "volume_id": req_params.get("volume_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateTenantVolumes(request):
    """ Updates a volume.
        Method:PUT
        URI:/v2/{tenant_id}/volumes/{volume_id}
    """
    data = {
        "volume": {
            "name": "vol-003",
            "description": "This is yet, another volume."
        }
    }
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/volumes/%(volume_id)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "volume_id": "b0aec9ad-c2f0-4dfd-8249-c3d4a819097b"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteTenantVolumes(request):
    """ Deletes a specified volume.
        Method:DELETE
        URI:/v2/{tenant_id}/volumes/{volume_id}
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/volumes/%(volume_id)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "volume_id": "b0aec9ad-c2f0-4dfd-8249-c3d4a819097b"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_extendTenantVolumesSize(request):
    """ Extends the size of a specified volume to a new size requested in GB.
        Method:POST
        URI:/v2/{tenant_id}/volumes/{volume_id}/action
    """
    data = {
        "os-extend": {
            "new_size": 3
        }
    }
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/volumes/%(volume_id)s/action' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "volume_id": "b0aec9ad-c2f0-4dfd-8249-c3d4a819097b"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_listTenantVolumesTypes(request):
    """ Lists volume types.
        Method:GET
        URI:/v2/{tenant_id}/types
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/types' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createTenantVolumesTypes(request):
    """ Creates a volume type.
        Method:POST
        URI:/v2/{tenant_id}/types
    """
    data = {
        "volume_type": {
            "name": "vol-type-001",
            "extra_specs": {
                "capabilities": "gpu"
            }
        }
    }
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/types' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_showTenantVolumesTypes(request):
    """ Shows information about a specified volume type.
        Method:GET
        URI:/v2/{tenant_id}/types/{volume_type_id}
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/types/%(volume_type_id)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "volume_type_id": "1a633a62-5a5a-45ab-b714-320d2a601f42"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_deleteTenantVolumesTypes(request):
    """ Deletes a specified volume type.
        Method:
        URI:/v2/{tenant_id}/types/{volume_type_id}
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/types/%(volume_type_id)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "volume_type_id": "1a633a62-5a5a-45ab-b714-320d2a601f42"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createTenantVolumesSnapshots(request):
    """ Creates a snapshot, which is a point-in-time complete copy of a volume. You can create a volume from the snapshot.
        Method:POST
        URI:/v2/{tenant_id}/snapshots{?snapshot,volume_id,force,name,description}
    """
    data = {
        "snapshot": {
            "name": "snap-001",
            "description": "Daily backup",
            "volume_id": "5aa119a8-d25b-45a7-8d1b-88e127885635",
            "force": True
        }
    }
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/snapshots' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_listTenantVolumesSnapshots(request):
    """ Lists summary information for all Block Storage snapshots that the tenant who submits the request can access.
        Method:GET
        URI:/v2/{tenant_id}/snapshots
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/snapshots' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailTenantVolumesSnapshots(request):
    """ Lists detailed information for all Block Storage snapshots that the tenant who submits the request can access.
        Method:GET
        URI:/v2/{tenant_id}/snapshots/detail
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/snapshots/detail' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_showTenantVolumesSnapshots(request):
    """ Shows information for a specified snapshot.
        Method:GET
        URI:/v2/{tenant_id}/snapshots/{snapshot_id}
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/snapshots/%(snapshot_id)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "snapshot_id": "63127c80-3e62-4f94-b9f4-5999bdd1b3b2"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateTenantVolumesSnapshots(request):
    """ Updates a specified snapshot.
        Method:PUT
        URI:/v2/{tenant_id}/snapshots/{snapshot_id}
    """
    data = {
        "snapshot": {
            "name": "snap-002",
            "description": "This is yet, another snapshot."
        }
    }
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/snapshots/%(snapshot_id)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "snapshot_id": "63127c80-3e62-4f94-b9f4-5999bdd1b3b2"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteTenantVolumesSnapshots(request):
    """ Deletes a specified snapshot.
        Method:DELETE
        URI:/v2/{tenant_id}/snapshots/{snapshot_id}
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/snapshots/%(snapshot_id)s' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "snapshot_id": "63127c80-3e62-4f94-b9f4-5999bdd1b3b2"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_showTenantVolumesSnapshotsMetadata(request):
    """ Shows the metadata for a specified snapshot.
        Method:GET
        URI:/v2/{tenant_id}/snapshots/{snapshot_id}/metadata
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/snapshots/%(snapshot_id)s/metadata' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "snapshot_id": "63127c80-3e62-4f94-b9f4-5999bdd1b3b2"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateTenantVolumesSnapshotsMetadata(request):
    """ Updates the metadata for a specified snapshot.
        Method:PUT
        URI:/v2/{tenant_id}/snapshots/{snapshot_id}/metadata
    """
    data = {
        "metadata": {
            "key": "v2"
        }
    }
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/snapshots/%(snapshot_id)s/metadata' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
            "snapshot_id": "63127c80-3e62-4f94-b9f4-5999bdd1b3b2"
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_createTenantVolumesQos(request):
    """ Creates a QoS specification.
        Method:POST
        URI:/v2/{tenant_id}/qos-specs
    """
    data = {
        "qos_specs": {
            "availability": "100",
            "name": "reliability-spec",
            "numberOfFailures": "0"
        }
    }
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/qos-specs' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_listTenantVolumesQos(request):
    """ Lists quality of service (QoS) specifications.
        Method:GET
        URI:/v2/{tenant_id}/qos-specs
    """
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/qos-specs' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_detailTenantVolumesQos(request):
    """ Shows details for a specified QoS specification.
        Method:GET
        URI:/v2/{tenant_id}/qos-specs/{qos_id}
    """
    pass


def v2_deleteTenantVolumesQos(request):
    """ Deletes a specified QoS specification.
        Method:DELETE
        URI:/v2/{tenant_id}/qos-specs/{qos_id}
    """
    pass


def v2_associateTenantVolumesQos(request):
    """ Associates a QoS specification with a specified volume type.
        Method:GET
        URI:/v2/{tenant_id}/qos-specs/{qos_id}/associate{?vol_type_id}
    """
    pass


def v2_disassociateTenantVolumesQos(request):
    """ Disassociates a QoS specification from a specified volume type.
        Method:GET
        URI:/v2/{tenant_id}/qos-specs/{qos_id}/disassociate{?vol_type_id}
    """
    pass


def v2_alldisassociateallTenantVolumesQos(request):
    """ Disassociates a specified QoS specification from all associations.
        Method:GET
        URI:/v2/{tenant_id}/qos-specs/{qos_id}/disassociate_all
    """
    pass


def v2_allassociationsTenantVolumesQos(request):
    """ Gets all associations for a specified QoS specification.
        Method:GET
        URI:/v2/{tenant_id}/qos-specs/{qos_id}/associations
    """
    pass


def v2_showTenantVolumesOsquotasets(request):
    """ Shows quotas for a tenant.
        Method:GET
        URI:/v2/{tenant_id}/os-quota-sets/{tenant_id}
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
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/os-quota-sets/%(tenant_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateTenantVolumesOsquotasets(request):
    """ Updates quotas for a tenant.
        Method:PUT
        URI:/v2/{tenant_id}/os-quota-sets/{tenant_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id")
    }
    data = {
        "quota_set": {
            "backups": 15
        }
    }
    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/os-quota-sets/%(tenant_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.putData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)


def v2_deleteTenantVolumesOsquotasets(request):
    """ Deletes quotas for a tenant so the quotas revert to default values.
        Method:DELETE
        URI:/v2/{tenant_id}/os-quota-sets/{tenant_id}
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/os-quota-sets/%(tenant_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.deleteData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_defaulteTenantVolumesOsquotasets(request):
    """ Gets default quotas for a tenant.
        Method:GET
        URI:/v2/{tenant_id}/os-quota-sets/defaults
    """
    req_params = {
        "token_id": request.POST.get("token_id"),
        "remotehost": request.POST.get("remotehost"),
        "tenant_id": request.POST.get("tenant_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/os-quota-sets/defaults' % {
            "tenant_id": req_params.get("tenant_id"),
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_showTenantVolumesOsquotasetsUser(request):
    """ Enables an admin user to show quotas for a specified tenant and user.
        Method:GET
        URI:/v2/{tenant_id}/os-quota-sets/{tenant_id}/{user_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "user_id": request.GET.get("user_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/os-quota-sets/%(tenant_id)s/%(user_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "user_id": req_params.get("user_id"),
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_updateTenantVolumesOsquotasetsUser(request):
    """ Updates quotas for a specified tenant/project and user.
        Method:POST
        URI:/v2/{tenant_id}/os-quota-sets/{tenant_id}/{user_id}
    """
    pass


def v2_deleteTenantVolumesOsquotasetsUser(request):
    """ Deletes quotas for a user so that the quotas revert to default values.
        Method:DELETE
        URI:/v2/{tenant_id}/os-quota-sets/{tenant_id}/{user_id}
    """
    pass


def v2_detailTenantVolumesOsquotasetsUser(request):
    """ Shows details for quotas for a specified tenant and user.
        Method:GET
        URI:/v2/{tenant_id}/os-quota-sets/{tenant_id}/detail/{user_id}
    """
    req_params = {
        "token_id": request.GET.get("token_id"),
        "remotehost": request.GET.get("remotehost"),
        "tenant_id": request.GET.get("tenant_id"),
        "user_id": request.GET.get("user_id")
    }

    head = [
        "X-Auth-Token: %s" % req_params.get("token_id"),
    ]
    parms = {
        'servername': req_params.get("remotehost"),
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/os-quota-sets/%(tenant_id)s/detail/%(user_id)s' % {
            "tenant_id": req_params.get("tenant_id"),
            "user_id": req_params.get("user_id")
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_showTenantAbsoluteLimits(request):
    """ Shows absolute limits for a tenant.
        Method:GET
        URI:/v2/{tenant_id}/limits
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
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/limits' % {
            "tenant_id": req_params.get("tenant_id"),
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.getData(hpc.initCurl(), url, head)
    return HttpResponse(context)


def v2_createTenantVolumesOsvolumemanage(request):
    """ Creates a Block Storage volume using existing storage instead of creating new storage.
        Method:POST
        URI:/v2/{tenant_id}/os-volume-manage
    """
    data = {
        "volume": {
            "host": "geraint-VirtualBox",
            "ref": {
                "source-volume-name": "existingLV",
                "source-volume-id": "1234"
            },
            "name": "New Volume",
            "availability_zone": "az2",
            "description": "Volume imported from existingLV",
            "volume_type": None,
            "bootable": "True",
            "metadata": {
                "key1": "value1",
                "key2": "value2"
            }
        }
    }
    token_id = 'e839a2fd51844fffaba95443bc0f25f0'

    head = [
        "X-Auth-Token: %s" % token_id,
    ]
    parms = {
        'servername': '192.168.30.127',
        'port': 8776,
        'uri': '/v2/%(tenant_id)s/os-volume-manage' % {
            "tenant_id": "ee3fcc7fab4e4e0690bcb560c26dfd03",
        }
    }
    url = 'http://%(servername)s:%(port)d%(uri)s' % parms
    hpc = HandlePycurl()
    context = hpc.postData(hpc.initCurl(), url, json.dumps(data), head)
    return HttpResponse(context)
