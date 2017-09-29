from django.test import TestCase


class PageExistTest(TestCase):


	def test_home_page_exists(self):
		response = self.client.get('/')
		self.assertFalse(response.status_code == 404)

	def test_about_me_page_exists(self):
		response = self.client.get('/about-me')
		self.assertFalse(response.status_code == 404)

	def test_gallery_page_exist(self):
		response = self.client.get('/gallery')
		self.assertFalse(response.status_code == 404)

	def test_commissions_page_exists(self):
		response = self.client.get('/how-to-order')
		self.assertFalse(response.status_code == 404)

	def test_blog_page_exist(self):
		response = self.client.get('/blog')
		self.assertFalse(response.status_code == 404)

	def test_contact_mark_page_exists(self):
		response = self.client.get('/contact-mark')
		self.assertFalse(response.status_code == 404)

	def test_links_page_exists(self):
		response = self.client.get('/links')
		self.assertFalse(response.status_code == 404)

	def test_buy_a_necklace_page_exists(self):
		response = self.client.get('/buy-a-necklace')
		self.assertFalse(response.status_code == 404)

	def test_view_cart_page_exists(self):
		response = self.client.get('/view-cart')
		self.assertFalse(response.status_code == 404)
		
