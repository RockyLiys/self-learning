from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
def seletevalue(value,num):
	return value[int(num)]
	

