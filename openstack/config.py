# coding=utf-8

def pr(dd):
    l, c = [], []
    for i, x in enumerate(dd):
        c.append(x)
        if len(c) == 2:
            l.append(c)
            c = []
    if len(dd) % 2 != 0:
        l.append([dd[-1]])
    return l


configs = {

    "v3/identity/auth/tokens/obtain/": {
        "lable_list": pr(["remotehost", "admin_name", "admin_pwd", "project_name"]),
        "method": "POST"
    },
    "v3/identity/domains/add/": {
        "lable_list": pr(["token_id", "remotehost", "domain_name", "domain_desc"]),
        "method": "POST"
    },
    "v3/identity/domains/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v3/identity/projects/add/": {
        "lable_list": pr(["token_id", "remotehost", "domain_id", "pro_name", "pro_desc"]),
        "method": "POST"
    },
    "v3/identity/projects/list/": {
        "lable_list": pr(["token_id", "remotehost", "role_name"]),
        "method": "GET"
    },
    "v3/identity/projects/details/": {
        "lable_list": pr(["token_id", "remotehost", "project_id"]),
        "method": "GET"
    },
    "v3/identity/projects/users/roles/list/": {
        "lable_list": pr(["token_id", "remotehost", "project_id", "user_id"]),
        "method": "GET"
    },
    "v3/identity/projects/users/roles/grant/": {
        "lable_list": pr(["token_id", "remotehost", "project_id", "user_id", "role_id"]),
        "method": "POST"
    },
    "v3/identity/projects/users/roles/revoke/": {
        "lable_list": pr(["token_id", "remotehost", "project_id", "user_id", "role_id"]),
        "method": "POST"
    },
    "v3/identity/users/add/": {
        "lable_list": pr(["token_id", "remotehost", "project_id", "domain_id", "user_name", "user_pwd", "user_email", "desc"]),
        "method": "POST"
    },
    "v3/identity/users/projects/list/": {
        "lable_list": pr(["token_id", "remotehost", "user_id"]),
        "method": "GET"
    },
    "v3/identity/roles/list/": {
        "lable_list": pr(["token_id", "remotehost", 'role_name']),
        "method": "GET"
    },
    "v3/identity/roles/detail/": {
        "lable_list": pr(["token_id", "remotehost", 'role_id']),
        "method": "GET"
    },
    ##########################################################################

    "v2/identity/obtainToken/": {
        "lable_list": pr(["remotehost", "tenantName", "username", "password"]),
        "method": "POST",
    },
    "v2/identity/validateToken/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/identity/tenants/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/identity/tenants/detailByName/": {
        "lable_list": pr(["token_id", "remotehost", "tenantName"]),
        "method": "GET"
    },
    "v2/identity/tenants/detailById/": {
        "lable_list": pr(["token_id", "remotehost", "tenantId"]),
        "method": "GET"
    },
    "v2/identity/tenants/create/": {
        "lable_list": pr(["token_id", "remotehost", "tenantName", "description"]),
        "method": "POST"
    },
    "v2/identity/tenants/update/": {
        "lable_list": pr(["token_id", "remotehost", "tenantName", "description", "tenantId"]),
        "method": "POST"
    },
    "v2/identity/tenants/delete/": {
        "lable_list": pr(["token_id", "remotehost", "tenantId"]),
        "method": "GET"
    },
    ##########################################################################

    "v2/identity/users/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/identity/users/add/": {
        "lable_list": pr(["token_id", "remotehost", "tenantId", "userId", "userName", "userEmail"]),
        "method": "POST"
    },
    "v2/identity/users/detailByName/": {
        "lable_list": pr(["token_id", "remotehost", "userName"]),
        "method": "GET"
    },
    "v2/identity/users/detailById/": {
        "lable_list": pr(["token_id", "remotehost", "userId"]),
        "method": "GET"
    },
    "v2/identity/users/update/": {
        "lable_list": pr(["token_id", "remotehost", "userId", "userName", "userEmail"]),
        "method": "POST"
    },
    "v2/identity/users/delete/": {
        "lable_list": pr(["token_id", "remotehost", "userId"]),
        "method": "POST"
    },
    "v2/identity/users/globalroles/list/": {
        "lable_list": pr(["token_id", "remotehost", "user_id"]),
        "method": "GET"
    },

    "v2/identity/tenants/users/roles/list": {
        "lable_list": pr(["token_id", "remotehost", "tenantId", "userId"]),
        "method": "GET"
    },

    "v2/identity/tenants/users/roles/OS-KSADM/add/": {
        "lable_list": pr(["token_id", "remotehost", "tenantId", "userId", "roleId"]),
        "method": "POST"
    },

    "v2/identity/tenants/users/roles/OS-KSADM/delete/": {
        "lable_list": pr(["token_id", "remotehost", "tenantId", "userId", "roleId"]),
        "method": "POST"
    },
    "v2/identity/OS-KSADM/roles/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/identity/OS-KSADM/roles/infobyid/": {
        "lable_list": pr(["token_id", "remotehost", "role_id"]),
        "method": "GET"
    },
    "v2/identity/OS-KSADM/roles/add/": {
        "lable_list": pr(["token_id", "remotehost", "role_id", "role_name", "role_description"]),
        "method": "POST"
    },
    "v2/identity/OS-KSADM/roles/delete/": {
        "lable_list": pr(["token_id", "remotehost", "role_id"]),
        "method": "POST"
    },
    "v2/identity/OS-KSADM/services/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    # "v2/identity/OS-KSADM/services/infobyname/":{
    # 	"lable_list":pr(["token_id","remotehost","service_name"]),
    # 	"method":"GET"
    # },
    "v2/identity/OS-KSADM/services/infobyid/": {
        "lable_list": pr(["token_id", "remotehost", "service_id"]),
        "method": "GET"
    },
    "v2/identity/OS-KSADM/services/add/": {
        "lable_list": pr(["token_id", "remotehost", "service_id", "service_name", "service_type", "service_desc"]),
        "method": "POST"
    },

    ##########################################################################

    "v2/tenant/volumes/osquotasets/show/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/tenant/volumes/osquotasets/update/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "POST"
    },
    "v2/tenant/volumes/osquotasets/delete/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "POST"
    },
    "v2/tenant/volumes/osquotasets/defaulte/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "POST"
    },
    "v2/tenant/volumes/osquotasets/user/show/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "user_id"]),
        "method": "GET"
    },
    "v2/tenant/absolutelimits/show/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/tenant/volumes/osquotasets/user/detail/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "user_id"]),
        "method": "GET"
    },
    "v2/tenant/volumes/create/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "volume_name", "volume_size"]),
        "method": "POST"
    },

    ###################################---compute---#######################################
    "v2/compute/extensions/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/extensions/detail/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "alias"]),
        "method": "GET"
    },

    "v2/compute/tenant/limits/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/servers/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/servers/create/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_name", "port", "imageRef_id", "network_uuid", "security_groups_name", ]),
        "method": "POST",
    },
    "v2/compute/tenants/allservers/detail/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/servers/detail/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/servers/update/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "POST"
    },

    "v2/compute/tenants/servers/vnc/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/start/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/stop/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/action/resize/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id", "flavor_id"]),
        "method": "POST"
    },

    "v2/compute/tenants/servers/action/reboot/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/delete/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/osfloatingips/add/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id", "floating_address"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/osfloatingips/remove/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id", "floating_address"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/volume/attach/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id", "volume_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/volume/detach/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id", "attachment_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/osfloatingips/pools/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },

    "v2/compute/tenants/os-keypairs/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/os-keypairs/show/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "keypair_name"]),
        "method": "GET"
    },
    "v2/compute/tenants/os-keypairs/delete/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "keypair_name"]),
        "method": "POST"
    },
    "v2/compute/tenants/os-keypairs/create/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "keypair_name"]),
        "method": "POST"
    },
    "v2/compute/tenants/os-keypairs/import/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "keypair_name", "public_key"]),
        "method": "POST"
    },

    "v2/compute/tenants/os-security-groups/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/os-security-groups/create/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "security_group_name", "description"]),
        "method": "POST"
    },
    "v2/compute/tenants/os-security-groups/update/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "security_group_id", "security_group_name", "description"]),
        "method": "POST"
    },
    "v2/compute/tenants/os-security-groups/detail/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "security_group_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/os-security-groups/delete/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "security_group_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/os-security-groups/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/os-security-group-rules/create/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "from_port", "to_port", "cidr", "ip_protocol", "parent_group_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/os-security-group-rules/delete/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "security_group_rule_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/osfloatingips/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/osfloatingips/show/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "floating_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/osfloatingips/allocate/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "pool_name"]),
        "method": "POST"
    },
    "v2/compute/tenants/osfloatingips/deallocate/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "floating_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/oshosts/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/flavors/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/flavors/detail/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "flavor_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/allflavors/detail/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/flavors/create/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "flavor_name", "ram_count", "vcpus_count", "disk_count", "is_public"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/os-interface/create": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id", "port_id"]),
        "method": "POST"
    },
    "v2/compute/tenants/servers/os-interface/list": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id"]),
        "method": "GET"
    },
    "v2/compute/tenants/servers/os-interface/attachment/delete": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "server_id", "attachment_id"]),
        "method": "POST"
    },
    "v2/compute/admin_tenants/os-quota-sets/defaults": {
        "lable_list": pr(["token_id", "remotehost", "admin_tenant_id", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/admin_tenants/os-quota-sets/detail": {
        "lable_list": pr(["token_id", "remotehost", "admin_tenant_id", "tenant_id"]),
        "method": "GET"
    },
    "v2/compute/admin_tenants/os-quota-sets/update": {
        "lable_list": pr(["token_id", "remotehost", "admin_tenant_id", "tenant_id", "key_pairs_count"]),
        "method": "POST"
    },

    #################################---images---#########################################

    "v2/images/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/images/detail/": {
        "lable_list": pr(["token_id", "remotehost", "image_id"]),
        "method": "GET"
    },

    ##########################################################################
    "v2/networks/extensions/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/networks/extensions/detail/": {
        "lable_list": pr(["token_id", "remotehost", "alias	"]),
        "method": "GET"
    },
    "v2/networks/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/networks/create/": {
        "lable_list": pr(["token_id", "remotehost", "network_name"]),
        "method": "POST"
    },
    "v2/networks/show/": {
        "lable_list": pr(["token_id", "remotehost", "network_id"]),
        "method": "GET"
    },
    "v2/networks/update/": {
        "lable_list": pr(["token_id", "remotehost", "network_id", "network_name"]),
        "method": "POST"
    },
    "v2/networks/delete/": {
        "lable_list": pr(["token_id", "remotehost", "network_id"]),
        "method": "POST"
    },
    "v2/networks/ports/list/": {
        "lable_list": pr(["token_id", "remotehost", "router_id"]),
        "method": "GET"
    },

    "v2/networks/ports/show/": {
        "lable_list": pr(["token_id", "remotehost", "port_id"]),
        "method": "GET"
    },
    "v2/networks/ports/create/": {
        "lable_list": pr(["token_id", "remotehost", "network_id", "port_name", "subnet_id", "ip_address"]),
        "method": "POST"
    },
    "v2/networks/ports/delete/": {
        "lable_list": pr(["token_id", "remotehost", "port_id"]),
        "method": "POST"
    },
    "v2/networks/ports/update/": {
        "lable_list": pr(["token_id", "remotehost", "port_id", "port_name", "security_group_id"]),
        "method": "POST"
    },

    "v2/networks/quotas/show/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/networks/quotas/update/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id", "subnet_count", "router_count", "network_count", "floatingip_count", "port_count"]),
        "method": "POST"
    },
    "v2/networks/quotas/reset/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "POST"
    },
    "v2/networks/routers/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/networks/routers/create/": {
        "lable_list": pr(["token_id", "remotehost", "network_id", "router_name"]),
        "method": "POST"
    },
    "v2/networks/routers/detail/": {
        "lable_list": pr(["token_id", "remotehost", "router_id"]),
        "method": "GET"
    },
    "v2/networks/routers/update/": {
        "lable_list": pr(["token_id", "remotehost", "network_id", "router_name", "router_id"]),
        "method": "POST"
    },
    "v2/networks/routers/delete/": {
        "lable_list": pr(["token_id", "remotehost", "router_id"]),
        "method": "POST"
    },
    "v2/networks/routers/interfaces/add/": {
        "lable_list": pr(["token_id", "remotehost", "router_id", "subnet_id", "port_id"]),
        "method": "POST"
    },
    "v2/networks/routers/interfaces/remove/": {
        "lable_list": pr(["token_id", "remotehost", "router_id", "subnet_id", "port_id"]),
        "method": "POST"
    },
    "v2/externalnetworks/routers/setgateway/": {
        "lable_list": pr(["token_id", "remotehost", "router_id", "network_id"]),
        "method": "POST"
    },
    "v2/externalnetworks/routers/cleargateway/": {
        "lable_list": pr(["token_id", "remotehost", "router_id"]),
        "method": "POST"
    },
    "v2/networks/floatingips/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/networks/floatingips/show/": {
        "lable_list": pr(["token_id", "remotehost", "floatingip_id"]),
        "method": "GET"
    },
    "v2/networks/floatingips/update/": {
        "lable_list": pr(["token_id", "remotehost", "floatingip_id", "port_id"]),
        "method": "POST"
    },
    "v2/networks/subnets/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/networks/subnets/show/": {
        "lable_list": pr(["token_id", "remotehost", "subnet_id"]),
        "method": "GET"
    },
    "v2/networks/subnets/update/": {
        "lable_list": pr(["token_id", "remotehost", "subnet_id", "subnet_name"]),
        "method": "POST"
    },
    "v2/networks/subnets/delete/": {
        "lable_list": pr(["token_id", "remotehost", "subnet_id"]),
        "method": "POST"
    },
    "v2/networks/subnets/create/": {
        "lable_list": pr(["token_id", 'remotehost', "network_id", "subnet_name", "ip_version", "cidr"]),
        "method": "POST"
    },
    "v2/networks/securitygroups/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/networks/securitygroups/create/": {
        "lable_list": pr(["token_id", "remotehost", "security_groups_name", "security_group_description"]),
        "method": "POST",
    },
    "v2/networks/securitygroups/show/": {
        "lable_list": pr(["token_id", "remotehost", "security_group_id"]),
        "method": "GET"
    },
    "v2/networks/securitygroups/delete/": {
        "lable_list": pr(["token_id", "remotehost", "security_group_id"]),
        "method": "POST"
    },
    "v2/networks/securitygroupsrules/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "GET"
    },
    "v2/networks/securitygroupsrules/show/": {
        "lable_list": pr(["token_id", "remotehost", "rules_security_groups_id"]),
        "method": "GET"
    },
    "v2/networks/securitygroupsrules/create/": {
        "lable_list": pr(["token_id", "remotehost", "security_group_id"]),
        "method": "POST"
    },
    "v2/networks/securitygroupsrules/delete/": {
        "lable_list": pr(["token_id", "remotehost", "rules_security_groups_id"]),
        "method": "POST"
    },
    "v2/images/create/": {
        "lable_list": pr(["token_id", "remotehost", "image_name", "image_file"]),
        "method": "POST"
    },
    "v2/networks/vpns/vpnservices/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "POST"
    },
    "v2/networks/vpns/vpnservices/create/": {
        "lable_list": pr(["token_id", "remotehost", "subnet_id", "router_id", "vpn_service_name"]),
        "method": "POST"
    },
    "v2/networks/vpns/vpnservices/remove/": {
        "lable_list": pr(["token_id", "remotehost", "service_id"]),
        "method": "POST"
    },
    "v2/networks/vpns/ipsecsiteconnections/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "POST"
    },
    "v2/networks/vpns/ipsecsiteconnections/remove/": {
        "lable_list": pr(["token_id", "remotehost", "ipsec_site_connection_id"]),
        "method": "POST"
    },
    "v2/networks/vpns/ipsecpolicies/list/": {
        "lable_list": pr(["token_id", "remotehost"]),
        "method": "POST"
    },

    "v2/networks/vpns/ipsecpolicies/create/": {
        "lable_list": pr(["token_id", "remotehost", "ipsecpolicie_name"]),
        "method": "POST"
    },
    "v2/networks/vpns/ipsecpolicies/show/": {
        "lable_list": pr(["token_id", "remotehost", "ipsecpolicy_id"]),
        "method": "POST"
    },
    "v2/networks/vpns/ipsecpolicies/remove/": {
        "lable_list": pr(["token_id", "remotehost", "ipsecpolicy_id"]),
        "method": "POST"
    },
    "v2/networks/vpns/ikepolicies/create/": {
        "lable_list": pr(["token_id", "remotehost", "ikepolicy_name"]),
        "method": "POST"
    },
    "v2/networks/vpns/ikepolicies/show/": {
        "lable_list": pr(["token_id", "remotehost", "ikepolicy_id"]),
        "method": "POST"
    },    
    "v2/networks/vpns/ikepolicies/remove/": {
        "lable_list": pr(["token_id", "remotehost", "ikepolicy_id"]),
        "method": "POST"
    },
    ##########################################################################
    "v2/tenant/volumes/list/": {
        "lable_list": pr(["token_id", "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/tenant/volumes/detail/": {
        "lable_list": pr(['token_id', "remotehost", "tenant_id"]),
        "method": "GET"
    },
    "v2/tenant/volumes/show/": {
        "lable_list": pr(['token_id', "remotehost", "tenant_id", "volume_id"]),
        "method": "GET"
    },


}
