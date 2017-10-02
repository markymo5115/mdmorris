from django.test import TestCase

# Create your tests here.
class TestBuyANecklaceView(TestCase):
	
	def test_buy_a_necklace_uses_correct_template(self):
		response = self.client.get('/buy-a-necklace')
		self.assertTemplateUsed(response, 'buy_a_necklace.html')

class Test_Cart_Checkout_View(TestCase):
	
	def test_view_cart_checkout_uses_correct_template(self):
		response = self.client.get('/view-cart')
		self.assertTemplateUsed(response, 'cart.html')
	
