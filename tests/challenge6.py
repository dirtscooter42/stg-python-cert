import unittest
from selenium import webdriver
from objects.homepage import HomePage


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.homepage = HomePage(webdriver.Chrome("../chromedriver.exe"))

    def tearDown(self):
        self.homepage.tear_down()

    def test_challenge6(self):
        self.homepage.set_up()
        results = self.homepage.search("Nissan")
        # print(results)
        try:
            self.assertIn("SKYLINE", self.homepage.get_make_results())
            # self.assertIn("ALTIMA", self.homepage.get_make_results())

        except AssertionError as error:
            print(error)
            self.homepage.take_screenshot("challenge6SearchResults")
            raise error


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
