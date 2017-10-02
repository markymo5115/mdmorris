from django.test import TestCase
#from projects.views import view_showcase, view_commission

# Create your tests here.
class TestShowCaseViews(TestCase):

	def test_uses_showcase_template(self):
		response = self.client.get('/gallery')
		self.assertTemplateUsed(response, 'showcase.html')


class TestCommissionsViews(TestCase):
	
	def test_uses_commissions_template(self):
		response = self.client.get('/how-to-order')
		self.assertTemplateUsed(response, 'commissions.html')


