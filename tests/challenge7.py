import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.wait import WebDriverWait


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()
        elements = WebDriverWait(self.driver, 10).until(cond.presence_of_all_elements_located((By.XPATH, "//div[@ng-if='popularSearches']//a")))
        trending_vehicles = self.driver.find_elements_by_xpath("//div[@ng-if='popularSearches']//a")

        print(elements)
        trending = []
        link = []

        for eachMake in trending_vehicles:
            print(eachMake.text)
            link.append(eachMake.get_attribute("href"))

        array_inception = zip(trending, link)
        print(trending)

        for each in array_inception:
            self.driver.get(each[1])
            each_trending_vehicle = WebDriverWait(self.driver, 10).until(cond.visibility_of_element_located((By.TAG_NAME, "tbody")))
            self.assertIn(each[0], each_trending_vehicle.text)
            if each == "More":
                pass
            else:
                print(f'{each[0]} is in {each[1]}')


if __name__ == '__main__':
    unittest.main()

    # Challenge 7 - Array / Dictionary.
    # One mistake that many people make in writing automation is making their script / objects too static. This causes a
    # maintenance nightmare when you have 1000 tests that need to be updated when a value changes or locators change.
    # This also posed a challenge when there are multiple languages involved but the page layout stays the same or if
    # the list of elements grows or shrinks. Arrays are great to use to create a virtual layout / map on navigation
    # objects like a top menu or multiple links in the footer.Rather than locating only one link, why not build a map
    # of all the links on a certain section.
    #
    # For this challenge, take a look at https://ww.copart.com main page. Go to the Makes / Models section of the
    # page. Create a 2 dimensional array that stores all the values displayed on the page along w / the URL for that
    # link. Once you have this array, you can verify all the elements in the array navigates to the correct page. To
    # get started, inspect the code and notice the section of the page is built using angular. There is no static id
    # or element class that identifies each element in this section. Everything is generic. The only way to build a
    # function / object for this section is to loop through each element. Hint: xpath is easiest.
    #
    # https: // www.w3schools.com / python / python_dictionaries.asp
    # https: // www.w3schools.com / python / python_arrays.asp
    #
    # ***make sure you make your code reusable.use
    #
    #
    # class and functions.
