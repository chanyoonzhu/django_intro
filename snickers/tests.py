from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse # dynamic url lookup

# Create your tests here.

class ThingsTests(SimpleTestCase):

    def test_home_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")