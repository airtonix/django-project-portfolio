from django import template
from django.db.models.loading import cache
from django.db.models import Model as DjangoModel

from classytags.core import Options
from classytags.arguments import (Argument, MultiValueArgument, MultiKeywordArgument)
from classytags.helpers import AsTag

from .. import models

register = template.Library()


@register.filter
def minus(value, args):
	try:
		return int(value) - int(args)

	except ValueError as error:
		return error


@register.filter
def fields(instance, args=None):
	try:
		return instance._meta.get_all_field_names()

	except ValueError as error:
		return error


@register.tag
class ProjectsQuerySetTag(AsTag):	 
	name = "get_projects"
	options = Options(
		MultiKeywordArgument('kwargs', resolve=True, required=False),
		'as',
		Argument('varname', resolve=False, required=False),
	)

	def get_value(self, context, kwargs=None, varname=None):
		count = 4
		if kwargs != None:
			tag = kwargs.get("tag", None)
			phase = kwargs.get("phase", None)
			count = kwargs.get("count", count)

		results = models.Project.objects.all()
		if tag != None: 
			results = results.filter(tags__name=tag)

		if phase != None: 
			results = results.filter(phase=phase)

		results = results[:count]

		return results


@register.tag
class ClientsQuerySetTag(AsTag):	 
	name = "get_clients"
	options = Options(
		MultiKeywordArgument('kwargs', resolve=True, required=False),
		'as',
		Argument('varname', resolve=False, required=False),
	)

	def get_value(self, context, kwargs=None, varname=None):
		count = 4
		if kwargs != None:
			tags = kwargs.get("tags", None)
			phase = kwargs.get("phase", None)
			count = kwargs.get("count", count)

		results = models.Client.objects.all()
		if tags != None: 
			results = results.filter(tags__name=tags)

		if type(count) == int:
			results = results[:count]

		return results

