from __future__ import unicode_literals
from django.conf.urls import url, include, patterns

import views as identity_views


urlpatterns = patterns(
    'openstack/identity',


    ########################################################
    #							V3
    ########################################################

    # tokens
    url(r'v3/identity/auth/tokens/obtain/', identity_views.v3_obtainAuthToken),
    url(r'v3/identity/auth/tokens/validate/', identity_views.v3_validateAuthToken),
    url(r'v3/identity/auth/tokens/check/', identity_views.v3_checkAuthToken),
    url(r'v3/identity/auth/tokens/revoke/', identity_views.v3_revokeAuthToken),

    # project
    url(r'v3/identity/projects/add/', identity_views.v3_addProject),
    url(r'v3/identity/projects/list/', identity_views.v3_listprojects),
    url(r'v3/identity/projects/details/', identity_views.v3_detailProject),
    url(r'v3/identity/projects/update/', identity_views.v3_updateProject),
    url(r'v3/identity/projects/delete/', identity_views.v3_deleteProject),
    # project/user/role
    url(r'v3/identity/projects/users/roles/list/', identity_views.v3_listProjectUserRole),
    url(r'v3/identity/projects/users/roles/grant/', identity_views.v3_grantProjectUserRole),
    url(r'v3/identity/projects/users/roles/check/', identity_views.v3_checkProjectUserRole),
    url(r'v3/identity/projects/users/roles/revoke/', identity_views.v3_revokeProjectUserRole),
    # project/group/role
    url(r'v3/identity/projects/groups/roles/list/', identity_views.v3_listProjectGroupRole),
    url(r'v3/identity/projects/groups/roles/grant/', identity_views.v3_grantProjectGroupRole),
    url(r'v3/identity/projects/groups/roles/check/', identity_views.v3_checkProjectGroupRole),
    url(r'v3/identity/projects/groups/roles/revoke/', identity_views.v3_revokeProjectGroupRole),

    # users

    url(r'v3/identity/users/add/', identity_views.v3_addUser),
    url(r'v3/identity/users/list/', identity_views.v3_listUsers),
    url(r'v3/identity/users/update/', identity_views.v3_updateUser),
    url(r'v3/identity/users/delete/', identity_views.v3_deleteUser),
    url(r'v3/identity/users/detail/', identity_views.v3_detailUser),

    # /users/groups
    url(r'v3/identity/users/groups/list/', identity_views.v3_listUserGroup),
    url(r'v3/identity/users/projects/list/', identity_views.v3_listUserProject),

    # groups
    url(r'v3/identity/groups/add/', identity_views.v3_addGroup),
    url(r'v3/identity/groups/list/', identity_views.v3_listGroups),
    url(r'v3/identity/groups/detail/', identity_views.v3_detailGroup),
    url(r'v3/identity/groups/update/', identity_views.v3_updateGroup),
    url(r'v3/identity/groups/delete/', identity_views.v3_deleteGroup),
    # /groups/users
    url(r'v3/identity/groups/users/list/', identity_views.v3_listGroupUsers),
    url(r'v3/identity/groups/users/add/', identity_views.v3_addUserToGroup),
    url(r'v3/identity/groups/users/remove/', identity_views.v3_removeUserFromGroup),
    url(r'v3/identity/groups/users/check/', identity_views.v3_validateUserInGroup),

    # credentials
    url(r'v3/identity/credentials/add/', identity_views.v3_addCredential),
    url(r'v3/identity/credentials/list/', identity_views.v3_listCredentials),
    url(r'v3/identity/credentials/detail/', identity_views.v3_detailCredential),
    url(r'v3/identity/credentials/update/', identity_views.v3_updateCredential),
    url(r'v3/identity/credentials/delete/', identity_views.v3_deleteCredential),

    # roles
    url(r'v3/identity/roles/add/', identity_views.v3_addRole),
    url(r'v3/identity/roles/list/', identity_views.v3_listRoles),
    url(r'v3/identity/roles/detail/', identity_views.v3_detailRoles),


    # policies
    url(r'v3/identity/policies/add/', identity_views.v3_addPolicies),
    url(r'v3/identity/policies/list/', identity_views.v3_listPolicies),
    url(r'v3/identity/policies/update/', identity_views.v3_updatePolicies),
    url(r'v3/identity/policies/detail/', identity_views.v3_detailPolicie),
    url(r'v3/identity/policies/delete/', identity_views.v3_deletePolicie),

    # domains
    url(r'v3/identity/domains/add/', identity_views.v3_addDomain),
    url(r'v3/identity/domains/list/', identity_views.v3_listDomains),
    url(r'v3/identity/domains/detail/', identity_views.v3_detailDomain),
    url(r'v3/identity/domains/update/', identity_views.v3_updateDomain),
    url(r'v3/identity/domains/delete/', identity_views.v3_deleteDomain),
    # domains/users/roles
    url(r'v3/identity/domains/users/roles/list/', identity_views.v3_listDomainUserRoles),
    url(r'v3/identity/domains/users/roles/grant/', identity_views.v3_grantDomainUserRoles),
    url(r'v3/identity/domains/users/roles/check/', identity_views.v3_checkDomainUserRoles),
    url(r'v3/identity/domains/users/roles/revoke/', identity_views.v3_revokeDomainUserRoles),
    # domains/
    url(r'v3/identity/domains/groups/roles/list/', identity_views.v3_listDomainGroupRoles),
    url(r'v3/identity/domains/groups/roles/grant/', identity_views.v3_grantDomainGroupRoles),
    url(r'v3/identity/domains/groups/roles/check/', identity_views.v3_checkDomainGroupRoles),
    url(r'v3/identity/domains/groups/roles/revoke/', identity_views.v3_revokeDomainGroupRoles),

    # endpoints
    url(r'v3/identity/endpoints/add/', identity_views.v3_addEndpoint),
    url(r'v3/identity/endpoints/list/', identity_views.v3_listEndpoints),
    url(r'v3/identity/endpoints/update/', identity_views.v3_updateEndpoint),
    url(r'v3/identity/endpoints/delete/', identity_views.v3_deleteEndpoint),

    # service catalog
    url(r'v3/identity/services/add/', identity_views.v3_addService),
    url(r'v3/identity/services/list/', identity_views.v3_listServices),
    url(r'v3/identity/services/detail/', identity_views.v3_detailService),
    url(r'v3/identity/services/update/', identity_views.v3_updateService),
    url(r'v3/identity/services/delete/', identity_views.v3_deleteService),

    ########################################################
    #							V2
    ########################################################

    # obtain token
    url(r'v2/identity/obtainToken/', identity_views.v2_obtainToken),
    url(r'v2/identity/listTokenTenants/', identity_views.v2_listTokenTenants),
    url(r'v2/identity/validateToken/', identity_views.v2_validateToken),
    # users
    url(r'v2/identity/users/list/', identity_views.v2_listUsers),
    url(r'v2/identity/users/add/', identity_views.v2_addUser),
    url(r'v2/identity/users/detailByName/', identity_views.v2_detailByNameUser),
    url(r'v2/identity/users/detailById/', identity_views.v2_detailByIdUser),
    url(r'v2/identity/users/update/', identity_views.v2_updateUser),
    url(r'v2/identity/users/delete/', identity_views.v2_deleteUser),
    # urses/role
    url(r'v2/identity/users/globalroles/list/', identity_views.v2_listUserGlobalRole),
    url(r'v2/identity/users/globalroles/OS-KSADM/add/', identity_views.v2_addGlobalRoleToUser),
    url(r'v2/identity/users/globalroles/OS-KSADM/delete/', identity_views.v2_deleteGlobalRoleFromUser),
    # tenants
    url(r'v2/identity/tenants/list/', identity_views.v2_listTenant),
    url(r'v2/identity/tenants/detailByName/', identity_views.v2_detailByNameTenant),
    url(r'v2/identity/tenants/detailById/', identity_views.v2_detailByIdTenant),
    url(r'v2/identity/tenants/create/', identity_views.v2_createTenant),
    url(r'v2/identity/tenants/update/', identity_views.v2_updateTenant),
    url(r'v2/identity/tenants/delete/', identity_views.v2_deleteTenant),
    # tenants/users/roles/
    url(r'v2/identity/tenants/users/roles/list', identity_views.v2_listTenantUserRoles),
    # tenants/users
    url(r'v2/identity/tenants/users/list/', identity_views.v2_listTenantUser),
    url(r'v2/identity/tenants/users/roles/OS-KSADM/add/', identity_views.v2_addTenantUserRole),
    url(r'v2/identity/tenants/users/roles/OS-KSADM/delete/', identity_views.v2_deleteTenantRoleFromUser),
    # roles
    url(r'v2/identity/OS-KSADM/roles/infobyname/', identity_views.v2_infoRoleByName),
    url(r'v2/identity/OS-KSADM/roles/list/', identity_views.v2_listRoles),
    url(r'v2/identity/OS-KSADM/roles/add/', identity_views.v2_addRole),
    url(r'v2/identity/OS-KSADM/roles/infobyid/', identity_views.v2_infoRoleById),
    url(r'v2/identity/OS-KSADM/roles/delete/', identity_views.v2_deleteRole),
    # servicess
    url(r'v2/identity/OS-KSADM/services/list/', identity_views.v2_listServices),
    url(r'v2/identity/OS-KSADM/services/add/', identity_views.v2_addService),
    url(r'v2/identity/OS-KSADM/services/infobyname/', identity_views.v2_infoServiceByName),
    url(r'v2/identity/OS-KSADM/services/infobyid/', identity_views.v2_infoServiceById),
    url(r'v2/identity/OS-KSADM/services/delete/', identity_views.v2_deleteService),

)
