import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")
        popular_items = self.driver.find_elements(By.CSS_SELECTOR, "li[ng-repeat*='popularSearch'] > a")
        for eachItem in popular_items:
            print(f'{eachItem.text} - {eachItem.get_attribute("href")}')

            assert len(popular_items) == 20


if __name__ == '__main__':
    unittest.main()