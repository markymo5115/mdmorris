from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from selenium import webdriver
from selenium.webdriver.firefox.webdriver  import WebDriver
from selenium.common.exceptions import WebDriverException
import time
import os

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):

	def setUp(self):
		#self.browser = webdriver.Firefox()
		self.browser = WebDriver()
		self.browser.implicitly_wait(MAX_WAIT)
		staging_server = os.environ.get('STAGING_SERVER')
		if staging_server:
			self.live_server_url = 'http://' + staging_server

	def tearDown(self):
		self.browser.quit()

