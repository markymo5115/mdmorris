from django.test import TestCase


class PageExistTest(TestCase):

	def test_home_page_exists(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
