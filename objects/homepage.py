from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:
    URL = 'https://www.copart.com'
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def setUp(self):
        self.browser.get(self.URL)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.close()

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
