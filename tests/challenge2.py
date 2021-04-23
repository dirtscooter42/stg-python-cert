import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium import webdriver


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_css_selector('input[id="input-search"]').send_keys('exotics')
        self.driver.find_element_by_css_selector('button[data-uname="homepageHeadersearchsubmit"]').click()
        table = WebDriverWait(self.driver, 10).until(cond.visibility_of_element_located((By.TAG_NAME, 'tbody')))
        self.assertIn("PORSCHE", table.text)


if __name__ == '__main__':
    unittest.main()