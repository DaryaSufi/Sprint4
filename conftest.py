import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture(params=['firefox','chrome'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.get(Constants.URL)
    elif request.param == 'chrome':
        browser =  webdriver.Chrome()
        browser.get(Constants.URL)
    else:
        raise ValueError('Unknown browser type')
    yield browser
    browser.quit()
