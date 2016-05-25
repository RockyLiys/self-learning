from __future__ import unicode_literals
from django.conf.urls import url, include, patterns

import views as images_views

urlpatterns = patterns(
    'openstack/images',

    # images/
    url(r'v2/images/create/', images_views.v2_createImages),
    url(r'v2/images/list/', images_views.v2_listImages),
    url(r'v2/images/detail/', images_views.v2_detailImages),
    url(r'v2/images/update/', images_views.v2_updateImages),
    url(r'v2/images/delete/', images_views.v2_deleteImages),

    # images/file
    url(r'v2/images/file/upload/', images_views.v2_uploadImagesFile),
    url(r'v2/images/file/download/', images_views.v2_downloadImagesFile),

    # images/tags
    url(r'v2/images/tags/add/', images_views.v2_addImagesTags),
    url(r'v2/images/tags/delete/', images_views.v2_deleteImagesTags),

    # images/members
    url(r'v2/images/members/add/', images_views.v2_addImagesMembers),
    url(r'v2/images/members/list/', images_views.v2_listImagesMembers),
    url(r'v2/images/members/detail/', images_views.v2_detailImagesMembers),
    url(r'v2/images/members/delete/', images_views.v2_deleteImagesMembers),
    url(r'v2/images/members/update/', images_views.v2_updateImagesMembers),

    # images/schemas/
    url(r'v2/images/schemas/images/', images_views.v2_getImagesSchemas),
    url(r'v2/images/schemas/image/', images_views.v2_getImagesSchema),
    # images/schemas/members/
    url(r'v2/images/schemas/members/', images_views.v2_getImagesSchemasMembers),
    url(r'v2/images/schemas/member/', images_views.v2_getImagesSchemasMember),





)
