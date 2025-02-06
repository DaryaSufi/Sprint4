import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture(params=['firefox','chrome'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser=  webdriver.Chrome()
    else:
        raise ValueError('Unknown browser type')
    yield browser
    browser.quit()
