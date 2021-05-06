import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.wait import WebDriverWait


class PracticeConcepts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_practiceConcepts(self):
        self.driver.get("https://www.motosport.com")
        # self.driver.maximize_window()
        elements = WebDriverWait(self.driver, 10).until(cond.presence_of_element_located)((By.CSS_SELECTOR, 'a[href="/all/health-and-fitness"]'))
        riding_gear = self.driver.find_elements_by_xpath('//*[@id="hpt"]/div/div[12]/div/div[2]/div[3]/ul')
        print(elements)

        # gear = []
        # link = []
        #
        # for gear_type in riding_gear:
        #     gear.append(gear_type.text)
        #     link.append(gear_type.get_attribute("href"))
        #
        # two_d_array = zip(gear, link)
        # print(two_d_array)


if __name__ == '__main__':
    unittest.main()
