from django.test import TestCase, Client
# Create your tests here.


class HomeTest(TestCase):

    def test_home(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 != 1)
        self.assertEquals(1, 1)
        self.assertIn(1, [1, 2, 3])

    def test_render(self):
        client = Client()
        response = client.get("/")
        self.assertEquals(response.status_code, 200)
        self.assertIn('products', response.context)
        products = response.context['products']
        self.assertEquals(len(products), 0)
