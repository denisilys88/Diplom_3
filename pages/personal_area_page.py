import allure
from pages.main_page import MainPage
from locators.login_page_locators import LoginPageLocators as LoginLoc
from locators.main_locators import MainLocators as MainLoc


class PersonalAreaPage(MainPage):

    @allure.step('Заполняем поле Email')
    def set_email(self, email):
        return self.find_element(LoginLoc.INPUT_MAIL).send_keys(email)

    @allure.step('Заполняем поле Пароль')
    def set_password(self, password):
        return self.find_element(LoginLoc.INPUT_PASSWORD).send_keys(password)

    @allure.step('Нажимаем кнопку Войти')
    def click_enter_button(self):
        return self.find_element(LoginLoc.ENTER_BUTTON, 20).click()

    @allure.step('Нажимаем на кнопку личный кабинет')
    def click_personal_area_button(self):
        return self.find_element(LoginLoc.PERSONAL_AREA_LINK, 20).click()

    @allure.step('Нажимаем на кнопку история заказов')
    def click_order_history_button(self):
        return self.find_element(LoginLoc.ORDER_HISTORY_BUTTON).click()

    @allure.step('Нажимаем кнопку выход')
    def click_exit_button(self):
        return self.find_element(LoginLoc.EXIT_BUTTON).click()

    @allure.step('Находим элемент история')
    def find_order_history(self):
        return self.find_element(LoginLoc.ORDER_HISTORY)

    @allure.step('Находим элемент Профиль')
    def find_profile(self):
        return self.find_element(LoginLoc.PROFILE)

    @allure.step('Находим кнопку Войти')
    def find_enter_button(self):
        return self.find_element(LoginLoc.ENTER_BUTTON)

    @allure.step('Находим кнопку Оформить заказ')
    def find_make_order_button(self):
        return self.find_element(MainLoc.MAKE_ORDER_BUTTON)
