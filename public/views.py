from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
import os
import json
from django.template import Context, loader,Template
from django.db import connection,transaction

from public import public_logger as logger


from api.settings import mongo_conn


def db_process(request):
	sql = "select is_superuser,username,password,first_name,last_name,email,is_staff,is_active from auth_user"
	cursor = connection.cursor()
	# cursor.callproc("test1")
	cursor.execute("select fun1()")
	raw = cursor.fetchall()
	# logger.debug(raw)
	data = {
		"data":raw
	}
	info = {
		"sql_ret":raw
	}
	# log = mongo_conn.log.public
	# log.insert(info)
	return HttpResponse(raw)





