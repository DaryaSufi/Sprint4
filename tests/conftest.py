import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()