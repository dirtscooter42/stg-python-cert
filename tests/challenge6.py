from idlelib import browser

import pytest
from _pytest import unittest

from objects import homepage
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as cond, wait

from objects.homepage import HomePage


@pytest.mark.usefixtures("browser")
class Challenge6(unittest.TestCase):
    homepage = HomePage(browser)

    def test_challenge6(self):
        homepage.setUp()
        self.driver.find_element_by_css_selector("input[id='input-search']").send_keys("nissan")
        self.driver.find_element_by_css_selector("button[data-uname='homepageHeadersearchsubmit']").click()
        # table = WebDriverWait(self.driver, 10).until(cond.visibility_of_element_located((By.TAG_NAME, 'tbody')))
        WebDriverWait(self.driver, 10).until(cond.visibility_of_element_located((By.TAG_NAME, 'tbody')))
        # self.assertIn("nissan", table.text)

        # waiting for loading wheel
        WebDriverWait(self.driver, 60).until(
            cond.invisibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable_processing\"]")))

        # expand the model search input box and search for "skyline".
        self.driver.find_element_by_xpath('//*[@data-uname="ModelFilter"]').click()
        models = self.driver.find_element_by_xpath('//*[@id="collapseinside4"]/form/div/input')
        models.send_keys("skyline")

        # verify that "skyline" is present in the search and take a screenshot
        try:
            WebDriverWait(self.driver, 10).until(cond.presence_of_element_located(By.ID, "lot_model_descSKYLINE"))
            print("The model 'Skyline' is present")
        except:
            self.driver.save_screenshot(f"../screenshots/screenshot.png")


if __name__ == '__main__':
    unittest.main()

# Challenge 6 - Error Handling
# Using a try/catch block can help you catch certain errors that might exist that you weren’t anticipating.  It can also
# give you some type of behavior you want to take when something happens.
#
# Let’s say you are running a test script and the 4th step fails.  At this point, you can decide what you want it to do.
# Do you want to try something else, or take a screenshot, or reset your browser of where you are at for the next step
# in the script?
#
# Taking a screenshot is a common way to use the try catch block.  For this challenge, go to copart site, search for
# nissan, and then for the model, search for “skyline”.  This is a rare car that might or might not be in the list for
# models.  When the link does not exist to click on, your script will throw an exception.  Catch the exception and take
# a screenshot of the page of what it looks like.
#
# https://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
# https://www.pythonforbeginners.com/error-handling/python-try-and-except
# https://www.w3schools.com/python/python_try_except.asp
# https://pythonspot.com/selenium-take-screenshot/
# https://www.pythonforbeginners.com/gui/how-to-use-pillow
# http://allselenium.info/capture-screenshot-element-using-python-selenium-webdriver/
