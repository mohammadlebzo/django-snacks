from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class SnacksTesting(SimpleTestCase):
    def test_page_status(self):
        home_response = self.client.get(reverse('home'))
        about_response = self.client.get(reverse('about'))
        self.assertEqual(home_response.status_code, 200)
        self.assertEqual(about_response.status_code, 200)

    def test_page_template(self):
        home_response = self.client.get(reverse('home'))
        about_response = self.client.get(reverse('about'))
        self.assertTemplateUsed(home_response, 'home.html')
        self.assertTemplateUsed(about_response, 'about.html')
