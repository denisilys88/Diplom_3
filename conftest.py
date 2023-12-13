import pytest
from selenium import webdriver
from locators.login_page_locators import LoginPageLocators as LoginLoc
from data import Data as D
from urls import Urls


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1200')
        firefox_options.add_argument('--height=800')
        driver = webdriver.Firefox(options=firefox_options)
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1200,800')
        driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(Urls.LOGIN_PAGE)
    driver.find_element(*LoginLoc.INPUT_MAIL).send_keys(D.EMAIL)
    driver.find_element(*LoginLoc.INPUT_PASSWORD).send_keys(D.PASSWORD)
    driver.find_element(*LoginLoc.ENTER_BUTTON).click()
    return driver
