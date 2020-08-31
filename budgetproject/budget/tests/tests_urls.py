from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import *


class TestUrls(SimpleTestCase):
    def test_list_url_resolves(self):
        ##does the reverse work
        url = reverse('list')
        self.assertEquals(resolve(url).func, project_list)

    def test_add_project_url_resolves(self):
        ##does the reverse work
        url = reverse('add')
        ##this is class based view so we add .view_class
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_project_detail_url_resolves(self):
        ##does the reverse work
        url = reverse('detail', args=['some-slug'])
        ##this is class based view so we add .view_class
        self.assertEquals(resolve(url).func, project_detail)
