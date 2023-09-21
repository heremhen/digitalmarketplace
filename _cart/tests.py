from django.test import TestCase

# Create your tests here.

from django.urls import reverse

class CartSummaryViewTest(TestCase):
    def test_cart_summary_view(self):
        response = self.client.get(reverse('cart-summary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart-summary.html')
        self.assertTrue('cart' in response.context)