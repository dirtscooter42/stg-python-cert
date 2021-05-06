import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as cond, wait

from objects.homepage import HomePage


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("../chromedriver.exe")
        self.homepage = HomePage(webdriver.Chrome("../chromedriver.exe"))

    def tearDown(self):
        self.browser.close()
        self.homepage.tear_down()

    def test_challenge5(self):
        self.homepage.set_up()
        results = self.homepage.search("PORSCHE")

        # change results value from 20 to 100
        self.homepage.change_search_count

        # waiting for loading wheel
        WebDriverWait(self.browser, 60).until(
            cond.invisibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable_processing\"]")))

        # results = self.driver.find_element_by_xpath("//*[@id='serverSideDataTable_info']")
        # print(results.text)

        models_returned = self.browser.find_elements(By.XPATH, "//span[@data-uname=\"lotsearchLotmodel\"]")
        damage_list = self.browser.find_elements(By.XPATH, "//span[@data-uname=\"lotsearchLotdamagedescription\"]")

        models_returned = []
        for model in models_returned:
            models_returned.append(model.text)
            values = [[model, models_returned.count(model)] for model in set(models_returned)]
        # print(values)

        damage = {
            "REAR END": 0,
            "FRONT END": 0,
            "MINOR DENT/SCRATCHES": 0,
            "UNDERCARRIAGE": 0,
            "All Other": 0
        }

        for damages in damage_list:
            if damages.text == "REAR END":
                damage["REAR END"] += 1
            elif damages.text == "FRONT END":
                damage["FRONT END"] += 1
            elif damages.text == "MINOR DENT/SCRATCHES":
                damage["MINOR DENT/SCRATCHES"] += 1
            elif damages.text == "UNDERCARRIAGE":
                damage["UNDERCARRIAGE"] += 1
            else:
                damage["All Other"] += 1
        for attribute, value in damage.items():
            print(f'{attribute} : {value}')
        pass


if __name__ == '__main__':
    unittest.main()



#
# Challenge 5 - If/Else/Switch Decision making is what will make your automation run w/ some AI helping it.  Rather
# than building a script w/ hard coded variables, why not use if/else/switch to do some basic decision making.  Let’s
# say, for a shopping scenario, I want to use Visa payment.  Then if I want to test MasterCard, should I write two
# sets of scripts?  Or should I write one script that depending on the data/card I want to use, the script will use
# if/else/switch to select the appropriate payment method for me.  This way, I will only have one script to maintain
# but I can write as many tests as I want that passes in a different set of data/variables that can be tested.  If
# someone changes the payment form, I would only have to update one set of code instead of multiple sets of code.
# This will help you make your automation more maintainable.  Another use in the decision making is to count bits of
# data.
#
# For this challenge, go to https://www.copart.com and do a search for “porsche” and change the  drop down for “Show
# Entries” to 100 from 20.  Count how many different models of porsche is in the results on the first page and return
# in the terminal how many of each type exists.
#
# Possible values can be “CAYENNE S”, “BOXSTER S”, etc.
#
# For the 2nd part of this challenge, create a switch statement to count the types of damages.
# Here’s the types:
# REAR END
# FRONT END
# MINOR DENT/SCRATCHES
# UNDERCARRIAGE
# And any other types can be grouped into one of MISC.
#
# https://www.w3schools.com/python/python_conditions.asp
# https://www.techbeamers.com/python-switch-case-statement/
# https://softwareengineering.stackexchange.com/questions/206816/clarification-of-avoid-if-else-advice
# https://en.wikipedia.org/wiki/Cyclomatic_complexity
# https://dzone.com/articles/code-smells-if-statements
# https://stackoverflow.com/questions/14555992/how-to-get-rid-of-if-else-statement-clutter
