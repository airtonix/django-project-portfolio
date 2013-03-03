from django.test import TestCase
from django.core.urlresolvers import reverse

from . import models


class ProjectsViewsTestCase(TestCase):


    def _generate_projects(self, **kwargs):
        tags = kwargs.pop("tags", None)
        for name in ("one", "two", "three", ):
            project = models.Project(title=name, slug=name, **kwargs)


    def test_index(self):
        self._generate_projects()
        resp = self.client.get(reverse('project-list'))
        self.assertEqual(resp.status_code, 200)


    def test_project_detail(self):
        name = "Glorious Test Dummy"
        slug = "glorious-test-dummy"

        project = models.Project(title = name, slug = slug)
        project.save()

        self.assertEqual(models.Project.objects.all().count(), 1)

        resp = self.client.get(project.get_absolute_url())
        self.assertEqual(resp.status_code, 200)

