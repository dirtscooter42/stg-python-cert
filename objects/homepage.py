from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond


class HomePage:
    URL = 'https://www.copart.com/'
    SEARCH_INPUT = (By.ID, 'input-search')
    SEARCH_RESULTS = (By.XPATH, '//table[@id="serverSideDataTable"]//tr')
    MAKES = (By.XPATH, "//table[@id='serverSideDataTable']//tr/td[5]")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def set_up(self):
        self.browser.get(self.URL)
        self.browser.maximize_window()

    def tear_down(self):
        self.browser.close()

    def search(self, phrase):
        search_input = self.wait.until(cond.visibility_of_element_located(self.SEARCH_INPUT))
        search_input.send_keys(phrase + Keys.RETURN)

    def get_make_results(self):
        elements = self.wait.until(cond.visibility_of_all_elements_located(
            (By.XPATH, "//table[@id='serverSideDataTable']//tr/td[5]")
        ))
        makes = []
        for el in elements:
            makes.append(el.text)
        print(makes)
        return makes

    def get_model_results(self):
        elements = self.wait.until(cond.visibility_of_all_elements_located(
            (By.XPATH, "//table[@id='serverSideDataTable']//tr/td[6]")
        ))
        models = []
        for el in elements:
            models.append(el.text)
        print(models)
        return models

    def take_screenshot(self, name):
        filepath = "../screenshots/" + name + ".png"
        self.browser.save_screenshot(filepath)

    def change_search_count(self):
        self.browser.find_element_by_xpath('//*[@id="serverSideDataTable_length"]/label/select'
                                           '/option[3]').click()
