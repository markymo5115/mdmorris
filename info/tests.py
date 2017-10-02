from django.test import TestCase

# Create your tests here.
class TestInfoViews(TestCase):
	
	def test_info_view_uses_correct_template(self):
		response = self.client.get('/links')
		self.assertTemplateUsed(response, 'links.html')
