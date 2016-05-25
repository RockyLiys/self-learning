
from django.db import connection,transaction


class HandleSql(object):
	"""docstring for ClassName"""
	def __init__(self, sql=None):
		self._sql = sql
	cursor = connection.cursor()           
	cursor.execute(self._sql)    
	raw = cursor.fetchone()  