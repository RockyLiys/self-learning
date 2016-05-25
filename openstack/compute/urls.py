# coding=utf-8
# from __future__ import unicode_literals
from django.conf.urls import url, include, patterns

import views as compute_views

urlpatterns = patterns(
    'openstack/compute',

    # compute/tenant/limits
    url(r'v2/compute/tenant/limits/list/', compute_views.v2_listComputeTenantLimits),
    # compute/tenant/extensions
    url(r'v2/compute/extensions/list/', compute_views.v2_listComputeExtensions),
    url(r'v2/compute/extensions/detail/', compute_views.v2_detailComputeExtension),
    # compute/tenants/servers
    url(r'v2/compute/tenants/servers/list/', compute_views.v2_listComputeTenantServers),
    url(r'v2/compute/tenants/servers/create/', compute_views.v2_createComputeTenantServer),
    url(r'v2/compute/tenants/allservers/detail/', compute_views.v2_detailComputeTenantAllServers),
    url(r'v2/compute/tenants/servers/detail/', compute_views.v2_detailComputeTenantServer),
    url(r'v2/compute/tenants/servers/update/', compute_views.v2_updateComputeTenantServer),
    url(r'v2/compute/tenants/servers/delete/', compute_views.v2_deleteComputeTenantServer),
    # extensions
    # vnc
    url(r'v2/compute/tenants/servers/vnc/', compute_views.v2_vncComputeTenantServer),
    # server start or stop
    url(r'v2/compute/tenants/servers/start/', compute_views.v2_startComputeTenantServer),
    url(r'v2/compute/tenants/servers/stop/', compute_views.v2_stopComputeTenantServer),
    # attaching or detach  volume to server
    url(r'v2/compute/tenants/servers/volume/attach/', compute_views.v2_attachComputeTenantServerVolume),
    url(r'v2/compute/tenants/servers/volume/detach/', compute_views.v2_detachComputeTenantServerVolume),

    # compute/tenants/serversMetadata
    url(r'v2/compute/tenants/serversMetadata/show/', compute_views.v2_showComputeTenantServerMetabata),
    url(r'v2/compute/tenants/serversMetadata/createOrReplace/', compute_views.v2_createOrReplaceComputeTenantServerMetabata),
    url(r'v2/compute/tenants/serversMetadata/update/', compute_views.v2_updateComputeTenantServerMetabata),
    url(r'v2/compute/tenants/serversMetadata/datail/', compute_views.v2_datailComputeTenantServerMetabata),
    url(r'v2/compute/tenants/serversMetadata/set/', compute_views.v2_setsComputeTenantServerMetabata),
    url(r'v2/compute/tenants/serversMetadata/delete/', compute_views.v2_deleteComputeTenantServerMetabata),
    # compute/tenants/servers/ips
    url(r'v2/compute/tenants/servers/ips/list/', compute_views.v2_listComputeTenantServerIps),
    url(r'v2/compute/tenants/servers/ips/addresses/list/', compute_views.v2_listComputeTenantServerIpsAddresses),
    # compute/tenants/servers/action
    url(r'v2/compute/tenants/servers/action/changepassword/', compute_views.v2_changepasswordComputeTenantServerAction),
    url(r'v2/compute/tenants/servers/action/reboot/', compute_views.v2_rebootComputeTenantServerAction),
    url(r'v2/compute/tenants/servers/action/rebuild/', compute_views.v2_rebuildComputeTenantServerAction),
    url(r'v2/compute/tenants/servers/action/resize/', compute_views.v2_resizeComputeTenantServerAction),
    url(r'v2/compute/tenants/servers/action/confirmResize/', compute_views.v2_confirmResizeComputeTenantServerAction),
    url(r'v2/compute/tenants/servers/action/revertResize/', compute_views.v2_revertResizeComputeTenantServerAction),
    url(r'v2/compute/tenants/servers/action/createImage/', compute_views.v2_createImageComputeTenantServerAction),

    # compute/tenants/flavors
    url(r'v2/compute/tenants/flavors/list/', compute_views.v2_listComputeTenantFlavors),
    url(r'v2/compute/tenants/allflavors/detail/', compute_views.v2_detailComputeTenantAllFlavors),
    url(r'v2/compute/tenants/flavors/detail/', compute_views.v2_detailComputeTenantFlavor),
    # extensions
    url(r'v2/compute/tenants/flavors/create/', compute_views.v2_createComputeTenantFlavor),
    # compute/tenants/images
    url(r'v2/compute/tenants/images/list/', compute_views.v2_listComputeTenantImages),
    url(r'v2/compute/tenants/allimages/detail/', compute_views.v2_detailComputeTenantAllImages),
    url(r'v2/compute/tenants/images/detail/', compute_views.v2_detailComputeTenantImage),
    url(r'v2/compute/tenants/images/delete/', compute_views.v2_deleteComputeTenantImage),
    # compute/tenants/imagesMetadata
    url(r'v2/compute/tenants/imagesMetadata/show/', compute_views.v2_showComputeTenantImagesMetadata),
    url(r'v2/compute/tenants/imagesMetadata/createOrReplace/', compute_views.v2_createOrReplaceComputeTenantImagesMetadata),
    url(r'v2/compute/tenants/imagesMetadata/update/', compute_views.v2_updateComputeTenantImagesMetadata),
    url(r'v2/compute/tenants/imagesMetadata/detail/', compute_views.v2_detailComputeTenantImagesMetadata),
    url(r'v2/compute/tenants/imagesMetadata/createOrUpdate/', compute_views.v2_createOrUpdateComputeTenantImagesMetadata),
    url(r'v2/compute/tenants/imagesMetadata/delete/', compute_views.v2_deleteComputeTenantImagesMetadata),

    # compute/tenants/keypairs
    url(r'v2/compute/tenants/os-keypairs/list/', compute_views.v2_listComputeTenantOskeypairs),
    url(r'v2/compute/tenants/os-keypairs/create/', compute_views.v2_createComputeTenantOskeypairs),
    url(r'v2/compute/tenants/os-keypairs/import/', compute_views.v2_importComputeTenantOskeypairs),
    url(r'v2/compute/tenants/os-keypairs/delete/', compute_views.v2_deleteComputeTenantOskeypairs),
    url(r'v2/compute/tenants/os-keypairs/show/', compute_views.v2_showComputeTenantOskeypairs),

    # compute/tenants/os-security-groups
    url(r'v2/compute/tenants/os-security-groups/list/', compute_views.v2_listComputeTenantOsSecuritygroups),
    url(r'v2/compute/tenants/os-security-groups/create/', compute_views.v2_createComputeTenantOsSecuritygroups),
    url(r'v2/compute/tenants/os-security-groups/detail/', compute_views.v2_detailComputeTenantOsSecuritygroups),
    url(r'v2/compute/tenants/os-security-groups/update/', compute_views.v2_updateComputeTenantOsSecuritygroups),
    url(r'v2/compute/tenants/os-security-groups/delete/', compute_views.v2_deleteComputeTenantOsSecuritygroups),
    url(r'v2/compute/tenants/servers/os-security-groups/list/', compute_views.v2_listComputeTenantServerOsSecuritygroups),

    # compute/tenants/os-security-group-rules
    url(r'v2/compute/tenants/os-security-group-rules/create/', compute_views.v2_createComputeTenantOsSecuritygroupsRules),
    url(r'v2/compute/tenants/os-security-group-rules/delete/', compute_views.v2_deleteComputeTenantOsSecuritygroupsRules),


    # compute/tenants/floatingips/pools
    url(r'v2/compute/tenants/osfloatingips/pools/list/', compute_views.v2_listComputeTenantsOsfloatingipsPools),
    # compute/tenants/floatingips/
    url(r'v2/compute/tenants/osfloatingips/list/', compute_views.v2_listComputeTenantsOsfloatingips),
    url(r'v2/compute/tenants/osfloatingips/allocate/', compute_views.v2_allocateComputeTenantsOsfloatingips),
    url(r'v2/compute/tenants/osfloatingips/show/', compute_views.v2_showComputeTenantsOsfloatingips),
    url(r'v2/compute/tenants/osfloatingips/deallocate/', compute_views.v2_deallocateComputeTenantsOsfloatingips),

    url(r'v2/compute/tenants/servers/osfloatingips/add/', compute_views.v2_addComputeTenantsServersOsfloatingips),
    url(r'v2/compute/tenants/servers/osfloatingips/remove/', compute_views.v2_removeComputeTenantsServersOsfloatingips),

    # compute/tenants/oshosts/
    url(r'v2/compute/tenants/oshosts/list/', compute_views.v2_listComputeTenantsOshosts),
    url(r'v2/compute/tenants/oshosts/show/', compute_views.v2_showComputeTenantsOshosts),
    url(r'v2/compute/tenants/oshosts/enableOrput/', compute_views.v2_enableOrputComputeTenantsOshosts),
    url(r'v2/compute/tenants/oshosts/start/', compute_views.v2_startComputeTenantsOshosts),
    url(r'v2/compute/tenants/oshosts/shutdown/', compute_views.v2_shutdownComputeTenantsOshosts),
    url(r'v2/compute/tenants/oshosts/reboot/', compute_views.v2_rebootComputeTenantsOshosts),

    # compute/tenants/servers/os-interface
    url(r'v2/compute/tenants/servers/os-interface/create', compute_views.v2_createOsInterfaceComputeTenantsServers),
    url(r'v2/compute/tenants/servers/os-interface/list', compute_views.v2_listOsInterfaceComputeTenantsServers),
    url(r'v2/compute/tenants/servers/os-interface/attachment/show', compute_views.v2_showAttachmentOsInterfaceComputeTenantsServers),
    url(r'v2/compute/tenants/servers/os-interface/attachment/delete', compute_views.v2_deleteAttachmentOsInterfaceComputeTenantsServers),

    # compute/tenant/os-quota-sets
    url(r'v2/compute/admin_tenants/os-quota-sets/defaults', compute_views.v2_DefaultsComputeTenantsQuota),
    url(r'v2/compute/admin_tenants/os-quota-sets/detail', compute_views.v2_DetailComputeTenantsQuota),
    url(r'v2/compute/admin_tenants/os-quota-sets/update', compute_views.v2_updateComputeTenantsQuota),




)
