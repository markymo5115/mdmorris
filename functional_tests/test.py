from .base import FunctionalTest
from unittest import skip
import time

class WebsiteStructureTest(FunctionalTest):

	def test_urls_are_all_there(self):
		# Mark goes to the wesite home pate and sees it exists
		self.browser.get(self.live_server_url)
		# he sees the correct title for the site
		assert 'English Enamel Box Miniature Paintings by Mark D Morris' in self.browser.title
		# he then types in the addresses of all the other pages in turn
		# The about me
		address = self.live_server_url + '/about-me'
		self.browser.get(address)
		assert 'About Mark' in self.browser.title

		self.browser.get(self.live_server_url + '/gallery/doorknobs')
		time.sleep(10)
		assert 'Doorknobs' in self.browser.title

		self.browser.get(self.live_server_url + '/how-to-order')
		assert 'commissions' in self.browser.title

		self.browser.get(self.live_server_url + '/blog')
		assert "MDMorris' Blog" in self.browser.title

		self.browser.get(self.live_server_url + '/contact-mark')
		assert 'Contact Mark' in self.browser.title

		self.browser.get(self.live_server_url + '/links')
		assert 'Links' in self.browser.title

		self.browser.get(self.live_server_url + '/buy-a-necklace')
		assert 'Colour Strip Necklace' in self.browser.title

		self.browser.get(self.live_server_url + '/view-cart')
		assert 'View Cart/Checkout' in self.browser.title


	def run_through_all_menu_links(self, address):
		self.browser.get(address)
		data = [("Home", "English Enamel Box Miniature Paintings by Mark D Morris"),
			("About Mark", "About Mark"),
		#	("Doorknobs", "Doorknobs"),
			("Commissions", "commissions"),
			("Blog", "MDMorris' Blog"),
			("Contact Mark", "Contact Mark"),
			("Links", "Links"),
			("Buy a Necklace", "Colour Strip Necklace"),
			("View Cart/Checkout", "View Cart/Checkout")]
			
		for d in data:
			self.browser.get(address)
			self.browser.find_element_by_link_text(d[0]).click()
			assert d[1] in self.browser.title

	@skip
	def test_all_the_menu_clicks_work(self):
		# Mark tests that all the menu links work on every page, he is very thorough!
		ad = self.live_server_url
		self.run_through_all_menu_links(ad)
		self.run_through_all_menu_links(ad + '/about-me')
		self.run_through_all_menu_links(ad + '/gallery/doorknobs')
		self.run_through_all_menu_links(ad + '/how-to-order')
		self.run_through_all_menu_links(ad + '/blog')
		self.run_through_all_menu_links(ad + '/contact-mark')
		self.run_through_all_menu_links(ad + '/buy-a-necklace')
		self.run_through_all_menu_links(ad + '/view-cart')

	@skip
	def test_gallery_displays_properly(self):
		# Mark goes to the gallery and sees some thumbnails of the work 
		# of this amazing enameller. 
		self.browser.get(self.live_server_url + '/gallery/doorknobs')
		#It is displayed nicely similar to Pinterest
		# and the thumbnails load quickly with new images loading when he scrolls down.
		
		
