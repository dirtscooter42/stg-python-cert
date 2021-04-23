import pytest

from selenium.webdriver import chrome
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope="class")
def browser():
    driver = webdriver.chrome()
    driver.implicitly_wait()
    yield driver
    driver.quit



