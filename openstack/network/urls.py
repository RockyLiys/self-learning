from __future__ import unicode_literals
from django.conf.urls import url, include, patterns

import views as network_views


urlpatterns = patterns(
    'openstack/network',

    # networks/
    url(r'v2/networks/list/', network_views.v2_listNetworks),
    url(r'v2/networks/create/', network_views.v2_createNetworks),
    url(r'v2/networks/multiple/create/', network_views.v2_createMultipleNetworks),
    url(r'v2/networks/show/', network_views.v2_showNetworks),
    url(r'v2/networks/update/', network_views.v2_updateNetworks),
    url(r'v2/networks/delete/', network_views.v2_deleteNetworks),
    # extensions
    url(r'v2/networks/multipleIncludeSegments/list/',
        network_views.v2_listNetworksMultipleIncludeSegments),
    url(r'v2/networks/multipleIncludeSegments/create/',
        network_views.v2_createNetworksMultipleIncludeSegments),
    url(r'v2/networks/multipleIncludeSegments/show/',
        network_views.v2_showNetworksMultipleIncludeSegments),

    # networks/subnets/
    url(r'v2/networks/subnets/list/', network_views.v2_listNetworksSubnets),
    url(r'v2/networks/subnets/create/', network_views.v2_createNetworksSubnets),
    url(r'v2/networks/subnets/multiple/create/', network_views.v2_createNetworksMultipleSubnets),
    url(r'v2/networks/subnets/show/', network_views.v2_showNetworksSubnets),
    url(r'v2/networks/subnets/update/', network_views.v2_updateNetworksSubnets),
    url(r'v2/networks/subnets/delete/', network_views.v2_deleteNetworksSubnets),
    # extensions

    # networks/ports/
    url(r'v2/networks/ports/list/', network_views.v2_listNetworksPorts),
    url(r'v2/networks/ports/create/', network_views.v2_createNetworksPorts),
    url(r'v2/networks/ports/multiple/create/', network_views.v2_createNetworksMultiplePorts),
    url(r'v2/networks/ports/show/', network_views.v2_showNetworksPorts),
    url(r'v2/networks/ports/update/', network_views.v2_updateNetworksPorts),
    url(r'v2/networks/ports/delete/', network_views.v2_deleteNetworksPorts),


    # extensions

    # network/extensions
    url(r'v2/networks/extensions/list/', network_views.v2_listNetworksExtensions),
    url(r'v2/networks/extensions/detail/', network_views.v2_detailNetworksExtensions),
    # metwork/quotas
    url(r'v2/networks/quotas/show/', network_views.v2_showNetworksQuotas),
    url(r'v2/networks/quotas/update/', network_views.v2_updateNetworksQuotas),
    url(r'v2/networks/quotas/reset/', network_views.v2_resetNetworksQuotas),

    # network/securitygroups/
    url(r'v2/networks/securitygroups/list/', network_views.v2_listNetworksSecuritygroups),
    url(r'v2/networks/securitygroups/create/', network_views.v2_createNetworksSecuritygroups),
    url(r'v2/networks/securitygroups/show/', network_views.v2_showNetworksSecuritygroups),
    url(r'v2/networks/securitygroups/delete/', network_views.v2_deleteNetworksSecuritygroups),
    # network/securitygroupsrules
    url(r'v2/networks/securitygroupsrules/list/', network_views.v2_listNetworksSecuritygroupsRules),
    url(r'v2/networks/securitygroupsrules/create/',
        network_views.v2_createNetworksSecuritygroupsRules),
    url(r'v2/networks/securitygroupsrules/show/', network_views.v2_showNetworksSecuritygroupsRules),
    url(r'v2/networks/securitygroupsrules/delete/',
        network_views.v2_deleteNetworksSecuritygroupsRules),

    # network/routers
    url(r'v2/networks/routers/list/', network_views.v2_listNetworksRouters),
    url(r'v2/networks/routers/create/', network_views.v2_createNetworksRouters),
    url(r'v2/networks/routers/detail/', network_views.v2_detailNetworksRouters),
    url(r'v2/networks/routers/update/', network_views.v2_updateNetworksRouters),
    url(r'v2/networks/routers/delete/', network_views.v2_deleteNetworksRouters),
    # network/routers/interface
    url(r'v2/networks/routers/interfaces/add/', network_views.v2_addNetworksRoutersInterfaces),
    url(r'v2/networks/routers/interfaces/remove/', network_views.v2_removeNetworksRoutersInterfaces),
    
    # network/router/setgateway
    url(r'v2/externalnetworks/routers/setgateway/', network_views.v2_addExternalNetworksRoutersSetGateway),
    url(r'v2/externalnetworks/routers/cleargateway/', network_views.v2_clearExternalNetworksRoutersClearGateway),

    # network/floatingips
    url(r'v2/networks/floatingips/list/', network_views.v2_listNetworksFloatingips),
    url(r'v2/networks/floatingips/create/', network_views.v2_createNetworksFloatingips),
    url(r'v2/networks/floatingips/show/', network_views.v2_showNetworksFloatingips),
    url(r'v2/networks/floatingips/update/', network_views.v2_updateNetworksFloatingips),
    url(r'v2/networks/floatingips/delete/', network_views.v2_deleteNetworksFloatingips),


    # network/loadbalancers/vips
    url(r'v2/networks/loadbalancers/vips/list/', network_views.v2_listNetworksLoadbalancersVips),
    url(r'v2/networks/loadbalancers/vips/create/', network_views.v2_createNetworksLoadbalancersVips),
    url(r'v2/networks/loadbalancers/vips/detail/', network_views.v2_detailNetworksLoadbalancersVips),
    url(r'v2/networks/loadbalancers/vips/update/', network_views.v2_updateNetworksLoadbalancersVips),
    url(r'v2/networks/loadbalancers/vips/delete/', network_views.v2_deleteNetworksLoadbalancersVips),

    # network/loadbalances/healthmonitors
    url(r'v2/networks/loadbalancers/healthmonitors/list/', network_views.v2_listNetworksLoadbalancersHealthmonitors),
    url(r'v2/networks/loadbalancers/healthmonitors/create/', network_views.v2_createNetworksLoadbalancersHealthmonitors),
    url(r'v2/networks/loadbalancers/healthmonitors/detail/', network_views.v2_detailNetworksLoadbalancersHealthmonitors),
    url(r'v2/networks/loadbalancers/healthmonitors/update/', network_views.v2_updateNetworksLoadbalancersHealthmonitors),
    url(r'v2/networks/loadbalancers/healthmonitors/delete/', network_views.v2_deleteNetworksLoadbalancersHealthmonitors),

    # network/loadbalancers/pools
    url(r'v2/networks/loadbalancers/pools/list/', network_views.v2_listNetworksLoadbalancersPools),
    url(r'v2/networks/loadbalancers/pools/create/', network_views.v2_createNetworksLoadbalancersPools),
    url(r'v2/networks/loadbalancers/pools/detail/', network_views.v2_detailNetworksLoadbalancersPools),
    url(r'v2/networks/loadbalancers/pools/update/', network_views.v2_updateNetworksLoadbalancersPools),
    url(r'v2/networks/loadbalancers/pools/delete/', network_views.v2_deleteNetworksLoadbalancersPools),
    # network/loadbalancers/pools/healthmonitors
    url(r'v2/networks/loadbalancers/pools/healthmonitors/associates/',
        network_views.v2_associatesNetworksLoadbalancersPoolsHealthmonitors),
    url(r'v2/networks/loadbalancers/pools/healthmonitors/disassociates/',
        network_views.v2_disassociatesNetworksLoadbalancersPoolsHealthmonitors),
    # network/loadbalancers/memters
    url(r'v2/networks/loadbalancers/memters/list/', network_views.v2_listNetworksLoadbalancersMemters),
    url(r'v2/networks/loadbalancers/memters/create/', network_views.v2_createNetworksLoadbalancersMemters),
    url(r'v2/networks/loadbalancers/memters/detail/', network_views.v2_detailNetworksLoadbalancersMemters),
    url(r'v2/networks/loadbalancers/memters/update/', network_views.v2_updateNetworksLoadbalancersMemters),
    url(r'v2/networks/loadbalancers/memters/delete/', network_views.v2_deleteNetworksLoadbalancersMemters),

    # network/lbaas/loadbalancers
    url(r'v2/networks/lbaas/loadbalancers/list/', network_views.v2_listNetworksLbaasLoadbalancers),
    url(r'v2/networks/lbaas/loadbalancers/create/', network_views.v2_createNetworksLbaasLoadbalancers),
    url(r'v2/networks/lbaas/loadbalancers/detail/', network_views.v2_detailNetworksLbaasLoadbalancers),
    url(r'v2/networks/lbaas/loadbalancers/update/', network_views.v2_updateNetworksLbaasLoadbalancers),
    url(r'v2/networks/lbaas/loadbalancers/remove/', network_views.v2_removeNetworksLbaasLoadbalancers),

    # networks/lbaas/listeners
    url(r'v2/networks/lbaas/listeners/list/', network_views.v2_listNetworksLbaasListeners),
    url(r'v2/networks/lbaas/listeners/create/', network_views.v2_createNetworksLbaasListeners),
    url(r'v2/networks/lbaas/listeners/detail/', network_views.v2_detailNetworksLbaasListeners),
    url(r'v2/networks/lbaas/listeners/update/', network_views.v2_updateNetworksLbaasListeners),
    url(r'v2/networks/lbaas/listeners/remove/', network_views.v2_removeNetworksLbaasListeners),

    # networks/lbaas/pools
    url(r'v2/networks/lbaas/pools/list/', network_views.v2_listNetworksLbaasPools),
    url(r'v2/networks/lbaas/pools/create/', network_views.v2_createNetworksLbaasPools),
    url(r'v2/networks/lbaas/pools/detail/', network_views.v2_detailNetworksLbaasPools),
    url(r'v2/networks/lbaas/pools/update/', network_views.v2_updateNetworksLbaasPools),
    url(r'v2/networks/lbaas/pools/remove/', network_views.v2_removeNetworksLbaasPools),

    # networks/lbaas/pools/memters
    url(r'v2/networks/lbaas/pools/memters/list/', network_views.v2_listNetworksLbaasPoolsMemters),
    url(r'v2/networks/lbaas/pools/memters/add/', network_views.v2_addNetworksLbaasPoolsMemters),
    url(r'v2/networks/lbaas/pools/memters/detail/', network_views.v2_detailNetworksLbaasPoolsMemters),
    url(r'v2/networks/lbaas/pools/memters/update/', network_views.v2_updateNetworksLbaasPoolsMemters),
    url(r'v2/networks/lbaas/pools/memters/remove/', network_views.v2_removeNetworksLbaasPoolsMemters),

    # networks/lbaas/healthmonitors
    url(r'v2/networks/lbaas/healthmonitors/list/', network_views.v2_listNetworksLbaasHealthmonitors),
    url(r'v2/networks/lbaas/healthmonitors/create/', network_views.v2_createNetworksLbaasHealthmonitors),
    url(r'v2/networks/lbaas/healthmonitors/detail/', network_views.v2_detailNetworksLbaasHealthmonitors),
    url(r'v2/networks/lbaas/healthmonitors/update/', network_views.v2_updateNetworksLbaasHealthmonitors),
    url(r'v2/networks/lbaas/healthmonitors/remove/', network_views.v2_removeNetworksLbaasHealthmonitors),



    # networks/vpns/ikepolicies
    url(r'v2/networks/vpns/ikepolicies/list/', network_views.v2_listNetworksVpnsIkepolicies),
    url(r'v2/networks/vpns/ikepolicies/create/', network_views.v2_createNetworksVpnsIkepolicies),
    url(r'v2/networks/vpns/ikepolicies/show/', network_views.v2_showNetworksVpnsIkepolicies),
    url(r'v2/networks/vpns/ikepolicies/update/', network_views.v2_updateNetworksVpnsIkepolicies),
    url(r'v2/networks/vpns/ikepolicies/remove/', network_views.v2_removeNetworksVpnsIkepolicies),

    # networks/vpns/ipsecpolicies
    url(r'v2/networks/vpns/ipsecpolicies/list/', network_views.v2_listNetworksVpnsIpsecpolicies),
    url(r'v2/networks/vpns/ipsecpolicies/create/', network_views.v2_createNetworksVpnsIpsecpolicies),
    url(r'v2/networks/vpns/ipsecpolicies/show/', network_views.v2_showNetworksVpnsIpsecpolicies),
    url(r'v2/networks/vpns/ipsecpolicies/update/', network_views.v2_updateNetworksVpnsIpsecpolicies),
    url(r'v2/networks/vpns/ipsecpolicies/remove/', network_views.v2_removeNetworksVpnsIpsecpolicies),

    # networks/vpns/vpnservices
    url(r'v2/networks/vpns/vpnservices/list/', network_views.v2_listNetworksVpnsVpnservices),
    url(r'v2/networks/vpns/vpnservices/create/', network_views.v2_createNetworksVpnsVpnservices),
    url(r'v2/networks/vpns/vpnservices/detail/', network_views.v2_detailNetworksVpnsVpnservices),
    url(r'v2/networks/vpns/vpnservices/update/', network_views.v2_updateNetworksVpnsVpnservices),
    url(r'v2/networks/vpns/vpnservices/remove/', network_views.v2_removeNetworksVpnsVpnservices),
    
    # networks/vpns/ipsecsiteconnections
    url(r'v2/networks/vpns/ipsecsiteconnections/list/', network_views.v2_listNetworksVpnsIpsecsiteconnections),
    url(r'v2/networks/vpns/ipsecsiteconnections/create/', network_views.v2_createNetworksVpnsIpsecsiteconnections),
    url(r'v2/networks/vpns/ipsecsiteconnections/show/', network_views.v2_showNetworksVpnsIpsecsiteconnections),
    url(r'v2/networks/vpns/ipsecsiteconnections/update/', network_views.v2_updateNetworksVpnsIpsecsiteconnections),
    url(r'v2/networks/vpns/ipsecsiteconnections/remove/', network_views.v2_removeNetworksVpnsIpsecsiteconnections),



)
