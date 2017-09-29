from django.test import TestCase


class PageExistTest(TestCase):


	def exists_or_redirect(self, status_code):
		true_or_false = (status_code == 200 or status_code == 302)
		if true_or_false == False:
			print(status_code)
		return true_or_false

	def test_home_page_exists(self):
		response = self.client.get('/')
		self.assertTrue(self.exists_or_redirect(response.status_code))

	def test_about_me_page_exists(self):
		response = self.client.get('/about-me')
		self.assertTrue(self.exists_or_redirect(response.status_code))
