print('open a new Firefox browser, \nload the page at the given URL')

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://selenium.dev/')


################################
print('open a new Firefox browser, \nload the Yahoo homepage, \nsearch for \"seleniumhq\", \nclose the browser')

#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()


###############################
import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)