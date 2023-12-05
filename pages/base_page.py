import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу по передаваемому url')
    def go_page(self, url):
        return self.driver.get(url)

    @allure.step('Ожидаем видимость передаваемого локатора')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f'Element wasnt found')

    @allure.step('Ожидаем отсутствие передаваемого локатора')
    def not_find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.none_of(EC.visibility_of_element_located(locator)),
                                                      message=f'Element was found')

    @allure.step('Возвращаем ожидаемый url')
    def get_current_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(url))

    @allure.step('Перетаскиваем элемент source в поле target')
    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
