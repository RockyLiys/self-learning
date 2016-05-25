from django import template

register = template.Library()

@register.simple_tag
def my_test(a,b):
	return a + b