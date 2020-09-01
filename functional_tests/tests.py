from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
	
    def setUp(self):
        self.browser = webdriver.Firefox()
		
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
		
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
		#page title and header mention 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
		#user is invited to enter a to-do list straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 
        'Enter a to-do item')
		#user types smt into text box
        inputbox.send_keys('Buy peacock feathers')
		#when user press Enter page will refresh and 
		#put to-do list in specified text into the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        #The page updates and there is a place holder still
        #inviting the user to enter a message user enter another 
        #message and press 'ENTER' the page updates and shows both items
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        self.fail('Finish Functional Test!')
