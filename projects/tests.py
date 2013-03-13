from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.utils.text import slugify

from mockups import Mockup, Factory

from . import models

import warnings

# class PartnerFactory(Factory):



class ProjectsTestMixin(object):
    project_mock = Mockup(models.Project, generate_fk=False, follow_m2m=False)
    client_mock = Mockup(models.Client, generate_fk=False, follow_m2m=False)

    def render(self, content, **context_kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            template = Template('{% load projects_tags %}' + content)
            context = Context(context_kwargs)
            return template.render(context)


class ViewsTestCase(ProjectsTestMixin, TestCase):

    def test_index(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.project_mock.create(100)
            resp = self.client.get(reverse('project-list'))
            self.assertEqual(resp.status_code, 200)


    def test_projects_detail(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.project_mock.create(1)
            project = models.Project.objects.get(pk = 1)
            resp = self.client.get(project.get_absolute_url())
            self.assertEqual(resp.status_code, 200)

    def test_clients_detail(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            self.client_mock.create(40)
            clients = models.Client.objects.all()

            client = clients.get(pk=1)
            resp = self.client.get(client.get_absolute_url())
            self.assertEqual(resp.status_code, 200)

            partner = clients.filter(tags__name__in = ["partner", ])
            if partner:
                resp = self.client.get(partner.get_absolute_url())
                self.assertEqual(resp.status_code, 200)



class TemplateTagsTestCase(ProjectsTestMixin, TestCase):

    def test_clients_as_variable(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            output = self.render("{% get_clients as Clients %}")
            print output