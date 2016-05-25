from __future__ import unicode_literals
from django.conf.urls import url, include, patterns

import views as volume_views

urlpatterns = patterns(
    'openstack/volumes',

    # volumes/extensions
    url(r'v2/volumes/extensions/', volume_views.v2_listVolumesExtensions),
    # tenant/volumes/
    url(r'v2/tenant/volumes/create/', volume_views.v2_createTenantVolumes),
    url(r'v2/tenant/volumes/list/', volume_views.v2_listTenantVolumes),
    url(r'v2/tenant/volumes/detail/', volume_views.v2_detailTenantVolumes),
    url(r'v2/tenant/volumes/show/', volume_views.v2_showTenantVolumes),
    url(r'v2/tenant/volumes/update/', volume_views.v2_updateTenantVolumes),
    url(r'v2/tenant/volumes/delete/', volume_views.v2_deleteTenantVolumes),
    url(r'v2/tenant/volumes/action/extendsize/', volume_views.v2_extendTenantVolumesSize),
    url(r'v2/tenant/volumes/types/list/', volume_views.v2_listTenantVolumesTypes),
    url(r'v2/tenant/volumes/types/create/', volume_views.v2_createTenantVolumesTypes),
    url(r'v2/tenant/volumes/types/show/', volume_views.v2_showTenantVolumesTypes),
    url(r'v2/tenant/volumes/types/delete/', volume_views.v2_deleteTenantVolumesTypes),

    # tenant/volumes/snapshots/
    url(r'v2/tenant/volumes/snapshots/create/', volume_views.v2_createTenantVolumesSnapshots),
    url(r'v2/tenant/volumes/snapshots/list/', volume_views.v2_listTenantVolumesSnapshots),
    url(r'v2/tenant/volumes/snapshots/detail/', volume_views.v2_detailTenantVolumesSnapshots),
    url(r'v2/tenant/volumes/snapshots/show/', volume_views.v2_showTenantVolumesSnapshots),
    url(r'v2/tenant/volumes/snapshots/update/', volume_views.v2_updateTenantVolumesSnapshots),
    url(r'v2/tenant/volumes/snapshots/delete/', volume_views.v2_deleteTenantVolumesSnapshots),
    # tenant/volumes/snapshotsmetadata
    url(r'v2/tenant/volumes/snapshotsmetadata/show/', volume_views.v2_showTenantVolumesSnapshotsMetadata),
    url(r'v2/tenant/volumes/snapshotsmetadata/update/', volume_views.v2_updateTenantVolumesSnapshotsMetadata),

    # tenant/volumes/qos
    url(r'v2/tenant/volumes/qos/create/', volume_views.v2_createTenantVolumesQos),
    url(r'v2/tenant/volumes/qos/list/', volume_views.v2_listTenantVolumesQos),
    url(r'v2/tenant/volumes/qos/detail/', volume_views.v2_detailTenantVolumesQos),
    url(r'v2/tenant/volumes/qos/delete/', volume_views.v2_deleteTenantVolumesQos),
    url(r'v2/tenant/volumes/qos/associate/', volume_views.v2_associateTenantVolumesQos),
    url(r'v2/tenant/volumes/qos/disassociate/', volume_views.v2_disassociateTenantVolumesQos),
    url(r'v2/tenant/volumes/qos/alldisassociate/', volume_views.v2_alldisassociateallTenantVolumesQos),
    url(r'v2/tenant/volumes/qos/allassociations/', volume_views.v2_allassociationsTenantVolumesQos),

    # tenant/volumes/osquotasets/
    url(r'v2/tenant/volumes/osquotasets/show/', volume_views.v2_showTenantVolumesOsquotasets),
    url(r'v2/tenant/volumes/osquotasets/update/', volume_views.v2_updateTenantVolumesOsquotasets),
    url(r'v2/tenant/volumes/osquotasets/delete/', volume_views.v2_deleteTenantVolumesOsquotasets),
    url(r'v2/tenant/volumes/osquotasets/defaulte/', volume_views.v2_defaulteTenantVolumesOsquotasets),
    # tenant/volumes/osquotasets/user/
    url(r'v2/tenant/volumes/osquotasets/user/show/', volume_views.v2_showTenantVolumesOsquotasetsUser),
    url(r'v2/tenant/volumes/osquotasets/user/update/', volume_views.v2_updateTenantVolumesOsquotasetsUser),
    url(r'v2/tenant/volumes/osquotasets/user/delete/', volume_views.v2_deleteTenantVolumesOsquotasetsUser),
    url(r'v2/tenant/volumes/osquotasets/user/detail/', volume_views.v2_detailTenantVolumesOsquotasetsUser),

    # tenant/volumes/limits
    url(r'v2/tenant/absolutelimits/show/', volume_views.v2_showTenantAbsoluteLimits),

    # tenant/volumes/osvolumemanage/
    url(r'v2/tenant/volumes/osvolumemanage/create/', volume_views.v2_createTenantVolumesOsvolumemanage),










)
