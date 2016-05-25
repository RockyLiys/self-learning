from __future__ import unicode_literals
from django.http import HttpResponse

from openstack.utils import HandlePycurl

import json

def v2_listMeteringsMeteringLabels(request):
	""" Lists all l3 metering labels that belong to the specified tenant.
		Method:GET
		URI:/v2.0/metering/metering-labels
	"""
	token_id = '2c769e9c9eea47c8bbd2c31712c51ba1'

	head = [
		"X-Auth-Token: %s"%token_id,
		]
	parms = {
		'servername':'192.168.30.127',
		'port':9696,
		'uri':'/v2.0/metering/metering-labels'
	}
	url = 'http://%(servername)s:%(port)d%(uri)s'%parms
	hpc = HandlePycurl()
	context = hpc.getData(hpc.initCurl(),url,head)
	return HttpResponse(context)

def v2_createMeteringsMeteringLabels(request):
	""" Creates a l3 metering label.
		Method:POST
		URI:/v2.0/metering/metering-labels
	"""
	data = {
		"metering_label": {
			"name": "label1",
			"description": "description of label1"
		}
	}
	token_id = '2c769e9c9eea47c8bbd2c31712c51ba1'

	head = [
		"X-Auth-Token: %s"%token_id,
		]
	parms = {
		'servername':'192.168.30.127',
		'port':9696,
		'uri':'/v2.0/metering/metering-labels'
	}
	url = 'http://%(servername)s:%(port)d%(uri)s'%parms
	hpc = HandlePycurl()
	context = hpc.postData(hpc.initCurl(),url,json.dumps(data),head)
	return HttpResponse(context)

def v2_showMeteringsMeteringLabels(request):
	""" Shows informations for a specified metering label.
		Method:GET
		URI:/v2.0/metering/metering-labels/{metering_label_id}
	"""
	token_id = '2c769e9c9eea47c8bbd2c31712c51ba1'

	head = [
		"X-Auth-Token: %s"%token_id,
		]
	parms = {
		'servername':'192.168.30.127',
		'port':9696,
		'uri':'/v2.0/metering/metering-labels/%(metering_label_id)s'%{
			"metering_label_id":"d185615d-821f-4d91-bd60-b9817f3d8540"
		}
	}
	url = 'http://%(servername)s:%(port)d%(uri)s'%parms
	hpc = HandlePycurl()
	context = hpc.getData(hpc.initCurl(),url,head)
	return HttpResponse(context)

def v2_deleteMeteringsMeteringLabels(request):
	""" Deletes a l3 metering label.
		Method:DELETE
		URI:/v2.0/metering/metering-labels/{metering_label_id}
	"""
	token_id = '2c769e9c9eea47c8bbd2c31712c51ba1'

	head = [
		"X-Auth-Token: %s"%token_id,
		]
	parms = {
		'servername':'192.168.30.127',
		'port':9696,
		'uri':'/v2.0/metering/metering-labels/%(metering_label_id)s'%{
			"metering_label_id":"d185615d-821f-4d91-bd60-b9817f3d8540"
		}
	}
	url = 'http://%(servername)s:%(port)d%(uri)s'%parms
	hpc = HandlePycurl()
	context = hpc.deleteData(hpc.initCurl(),url,head)
	return HttpResponse(context)

def v2_listMeteringsMeteringLabelsRules(request):
	""" Lists a summary of all l3 metering label rules belonging to the specified tenant.
		Method:GET
		URI:/v2.0/metering/metering-label-rules
	"""
	token_id = '2c769e9c9eea47c8bbd2c31712c51ba1'

	head = [
		"X-Auth-Token: %s"%token_id,
		]
	parms = {
		'servername':'192.168.30.127',
		'port':9696,
		'uri':'/v2.0/metering/metering-label-rules'
	}
	url = 'http://%(servername)s:%(port)d%(uri)s'%parms
	hpc = HandlePycurl()
	context = hpc.getData(hpc.initCurl(),url,head)
	return HttpResponse(context)


def v2_createMeteringsMeteringLabelsRules(request):
	""" Creates a l3 metering label rule.
		Method:POST
		URI:/v2.0/metering/metering-label-rules
	"""
	data = {
		"metering_label_rule": {
			"remote_ip_prefix": "10.0.1.0/24",
			"direction": "ingress",
			"metering_label_id": "448c774e-9dbc-4d31-a864-f85ecc19bb25"
		}
	}
	token_id = '2c769e9c9eea47c8bbd2c31712c51ba1'

	head = [
		"X-Auth-Token: %s"%token_id,
		]
	parms = {
		'servername':'192.168.30.127',
		'port':9696,
		'uri':'/v2.0/metering/metering-label-rules'
	}
	url = 'http://%(servername)s:%(port)d%(uri)s'%parms
	hpc = HandlePycurl()
	context = hpc.postData(hpc.initCurl(),url,json.dumps(data),head)
	return HttpResponse(context)

def v2_showMeteringsMeteringLabelsRules(request):
	""" Shows detailed informations for a specified metering label rule.
		Method:GET
		URI:/v2.0/metering/metering-label-rules/{metering_label_rule_id}
	"""
	token_id = '2c769e9c9eea47c8bbd2c31712c51ba1'

	head = [
		"X-Auth-Token: %s"%token_id,
		]
	parms = {
		'servername':'192.168.30.127',
		'port':9696,
		'uri':'/v2.0/metering/metering-label-rules/%(metering_label_rule_id)s'%{
			"metering_label_rule_id":"ca0d86f2-fbe8-4829-9cc1-847925677878"
		}
	}
	url = 'http://%(servername)s:%(port)d%(uri)s'%parms
	hpc = HandlePycurl()
	context = hpc.getData(hpc.initCurl(),url,head)
	return HttpResponse(context)

def v2_deleteMeteringsMeteringLabelsRules(request):
	""" Deletes a specified l3 metering label rule.
		Method:DELETE
		URI:/v2.0/metering/metering-label-rules/{metering-label-rule-id}
	"""
	token_id = '2c769e9c9eea47c8bbd2c31712c51ba1'

	head = [
		"X-Auth-Token: %s"%token_id,
		]
	parms = {
		'servername':'192.168.30.127',
		'port':9696,
		'uri':'/v2.0/metering/metering-label-rules/%(metering_label_rule_id)s'%{
			"metering_label_rule_id":"ca0d86f2-fbe8-4829-9cc1-847925677878"
		}
	}
	url = 'http://%(servername)s:%(port)d%(uri)s'%parms
	hpc = HandlePycurl()
	context = hpc.deleteData(hpc.initCurl(),url,head)
	return HttpResponse(context)

	
