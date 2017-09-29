from .base import FunctionalTest

class WebsiteStructureTest(FunctionalTest):

	def test_urls_are_all_there(self):
		# Mark goes to the wesite home pate and sees it exists
		self.browser.get(self.live_server_url)
		# he then types in the addresses of all the other pages in turn
		# The about me
		address = self.live_server_url + '/about-me'
		self.browser.get(address)
		assert 'About Mark' in self.browser.title

		self.browser.get(self.live_server_url + '/gallery')
		assert 'Explore the Gallery' in self.browser.title

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
