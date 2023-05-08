from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestPagina(TestCase):
    def test_RenderHtml(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Esse é o teste de página')