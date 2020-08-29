from selenium import webdriver
import unittest 
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):
	
    def setUp(self):
        self.browser = webdriver.Firefox()
		
    def tearDown(self):
        self.browser.quit()
		
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
		#page title and header mention 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
		#user is invited to enter a to-do list straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 
        'Enter a to-do item')
		#user types smt into text box
        inputbox.send_keys('1: Buy peacock feathers')
		#when user press Enter page will refresh and 
		#put to-do list in specified text into the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
		
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', 
            [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', 
            [row.text for row in rows])
        self.fail('Finish Functional Test!')
		
	
	
if __name__ == '__main__':
	unittest.main()
