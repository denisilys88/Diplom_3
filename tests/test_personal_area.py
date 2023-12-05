import allure
from pages.personal_area_page import PersonalAreaPage


class TestPersonalArea:

    @allure.title('Проверяем переход по клику в личный кабинет')
    @allure.description('Открываем страницу логина https://stellarburgers.nomoreparties.site/login, '
                        'логинимся, нажимаем кнопку "Войти", нажимаем кнопку "личный кабинет", '
                        'проверяем, что попали в личный кабинет')
    def test_transfer_to_personal_area_by_click(self, login):
        login_page = PersonalAreaPage(login)
        login_page.click_personal_area_button()
        assert login_page.find_profile()

    @allure.title('Проверяем переход в раздел История заказов')
    @allure.description('Открываем страницу логина https://stellarburgers.nomoreparties.site/login, '
                        'логинимся, нажимаем кнопку Войти, нажимаем кнопку "личный кабинет", '
                        'нажимаем кнопку "история заказов", проверяем, что открывается окно истории заказов')
    def test_transfer_to_order_history(self, login):
        login_page = PersonalAreaPage(login)
        login_page.click_personal_area_button()
        login_page.click_order_history_button()
        assert login_page.find_order_history()

    @allure.title('Проверяем выход из аккаунта')
    @allure.description('Открываем страницу логина https://stellarburgers.nomoreparties.site/login, '
                        'логинимся, нажимаем кнопку Войти, нажимаем кнопку "личный кабинет", '
                        'нажимаем кнопку "выход", проверяем, что вышли из аккаунта, появляется кнопка "Войти')
    def test_exit_button(self, login):
        login_page = PersonalAreaPage(login)
        login_page.click_personal_area_button()
        login_page.click_exit_button()
        assert login_page.find_enter_button()

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ')
    @allure.description('Открываем страницу https://stellarburgers.nomoreparties.site/login, логинимся'
                        'ожидаем, что на главной странице есть кнопка "Оформить заказ"')
    def test_login_user_can_make_order(self, login):
        login_page = PersonalAreaPage(login)
        assert login_page.find_make_order_button()



