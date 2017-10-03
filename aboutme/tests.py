from django.test import TestCase
#from aboutme.models import AboutMe
from aboutme.views import view_about_me
from django.core.urlresolvers import reverse


class ViewHomePageTest(TestCase):


	def test_uses_home_page_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')


	def run_through_menu_links(self, address):
		response = self.client.get(address)
		print(response.content.decode('utf8'))
		self.assertContains(response, '<a href="%s">' % reverse("home"), html=True )
		self.assertContains(response, '<a href="%s">' % reverse("about_me"), html=True )
		self.assertContains(response, '<a href="%s">' % reverse("gallery"), html=True )
		self.assertContains(response, '<a href="%s">' % reverse("commission"), html=True )
		self.assertContains(response, '<a href="%s">' % reverse("blog"), html=True )
		self.assertContains(response, '<a href="%s">' % reverse("contact-me"), html=True )
		self.assertContains(response, '<a href="%s">' % reverse("links"), html=True )
		self.assertContains(response, '<a href="%s">' % reverse("buy-a-necklace"), html=True )
		self.assertContains(response, '<a href="%s">' % reverse("view-cart"), html=True )

	def run_through_menu_links2(self, address):
		response = self.client.get(address)
		html = response.content.decode('utf8')
		#print(response.content.decode('utf8'))
		self.assertIn('<a href="%s">' % reverse("home"), html)
		self.assertIn('<a href="%s">' % reverse("about_me"), html)
		self.assertIn('<a href="%s">' % reverse("gallery"), html)
		self.assertIn('<a href="%s">' % reverse("commission"), html)
		self.assertIn('<a href="%s">' % reverse("blog"), html)
		self.assertIn('<a href="%s">' % reverse("contact-me"), html)
		self.assertIn('<a href="%s">' % reverse("links"), html)
		self.assertIn('<a href="%s">' % reverse("buy-a-necklace"), html)
		self.assertIn('<a href="%s">' % reverse("view-cart"), html)


	def test_home_page_has_correct_named_links(self):
		self.run_through_menu_links2(reverse("home"))

	def test_about_me_page_has_correct_menu_links(self):
		self.run_through_menu_links2(reverse("about_me"))

	def test_gallery_page_has_correct_menu_links(self):
		self.run_through_menu_links2(reverse("gallery"))

	def test_commission_page_has_correct_menu_links(self):
		self.run_through_menu_links2(reverse("commission"))

	def test_blog_page_has_correct_menu_links(self):
		self.run_through_menu_links2(reverse("blog"))

	def test_contact_me_page_has_correct_menu_links(self):
		self.run_through_menu_links2(reverse("contact-me"))

	def test_links_page_has_correct_menu_links(self):
		self.run_through_menu_links2(reverse("links"))

	def test_buy_a_necklace_has_correct_menu_links(self):
		self.run_through_menu_links2(reverse("buy-a-necklace"))

	def test_view_cart_has_correct_menu_links(self):
		self.run_through_menu_links2(reverse("view-cart"))

class ViewAboutMeTests(TestCase):

	def test_uses_aboutMe_template(self):
		response = self.client.get('/about-me')
		self.assertTemplateUsed(response, 'aboutme.html')


class ViewContactMe(TestCase):
	
	def test_uses_contactMe_template(self):
		response = self.client.get('/contact-mark')
		self.assertTemplateUsed(response, 'contactme.html')


