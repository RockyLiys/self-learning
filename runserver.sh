#!/bin/sh

# run site
read -p 'Input Web site Port:' PORT

#echo 'if blank ,Use default 8090 :'$PORT
if [ -f './manage.pyc' ];then
	./manage.pyc runserver 0.0.0.0:$PORT
else
	./manage.py runserver 0.0.0.0:$PORT
fi
