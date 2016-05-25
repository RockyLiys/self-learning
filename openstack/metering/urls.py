from __future__ import unicode_literals
from django.conf.urls import url, include,patterns

import views as metering_views


urlpatterns = patterns('openstack/metering',

	# meterings/meteringLabels
	url(r'v2/meterings/meteringLabels/list/',metering_views.v2_listMeteringsMeteringLabels),
	url(r'v2/meterings/meteringLabels/create/',metering_views.v2_createMeteringsMeteringLabels),
	url(r'v2/meterings/meteringLabels/show/',metering_views.v2_showMeteringsMeteringLabels),
	url(r'v2/meterings/meteringLabels/delete/',metering_views.v2_deleteMeteringsMeteringLabels),

	# meterings/meteringLabelsRules
	url(r'v2/meterings/meteringLabelsRules/list/',metering_views.v2_listMeteringsMeteringLabelsRules),
	url(r'v2/meterings/meteringLabelsRules/create/',metering_views.v2_createMeteringsMeteringLabelsRules),
	url(r'v2/meterings/meteringLabelsRules/show/',metering_views.v2_showMeteringsMeteringLabelsRules),
	url(r'v2/meterings/meteringLabelsRules/delete/',metering_views.v2_deleteMeteringsMeteringLabelsRules),


)