from django.test import TestCase
from django.urls import reverse


class HomeTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('home.index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Save the world!")

    def test_about_page(self):
        response = self.client.get(reverse('home.about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ABOUT US")
