Проект содержит тесты для сайта https://stellarburgers.nomoreparties.site/

Locators/login_page_locators::LoginPageLocators - содержит класс с константами локаторов страницы логина
Locators/main_locators::MainLocators - содержит класс с константами локаторов главной страницы
Locators/restore_page_locators::RestorePageLocators - содержит класс с константами локаторов страницы восстановления паролей

data/Data - класс с константами
url/Urls - класс с константами урлов

conftest.py содержит фикстуры:
driver - инициализирует драйвер Chrome, FireFox
login - инициализирует вход в учетную запись

requirements.txt - файл с зависимостями, используемые библиотеки:
pytest==6.2.1
selenium==4.13.0
allure-pytest==2.13.2
allure-python-commons==2.13.2

pages/base_page::BasePage - класс, описывающий базовые методы
pages/main_page::MainPage - класс, описывающий методы главной страницы
pages/personal_area_page::PersonalAreaPage - класс, описывающий методы личной страницы
pages/restore_password_page::RestorePasswordPage - класс, описывающий методы страницы восстановления пароля

[test_main_functions.py] содержит тесты на основной функционал
TestMainFunctions::test_transfer_by_click_constructor - проверяет переход в конструктор по кнопке "Конструктор
TestMainFunctions::test_transfer_by_click_order_line - проверяет переход на ленту заказов по кнопке "Лента заказов"
TestMainFunctions::test_show_ingredient_details - проверят, что клик по ингредиенту вызывает всплывающее окно с деталями
TestMainFunctions::test_close_ingredient_details - проверяет, что всплывающее окно закрывается кликом по крестику
TestMainFunctions::test_add_ingredient_counter - проверяет, что при добавлении ингредиента в заказ счётчик этого
ингредиента увеличивается

[test_order_line.py]
TestOrderLine::test_show_order_details - проверяет, что клик на заказ в ленте заказов вызывает всплывающее окно с
деталями заказа
TestOrderLine::test_show_orders_on_order_line - проверяет, что заказы пользователя из раздела «История заказов»
отображаются на странице «Лента заказов»
TestOrderLine::test_add_order_alltime_counter_increase - проверяет, что при создании нового заказа счётчик Выполнено за
всё время увеличивается'
TestOrderLine::test_add_order_day_counter_increase - проверяет, что при создании нового заказа счётчик Выполнено за
сегодня увеличивается
TestOrderLine::test_add_order_show_in_work - проверяет, что после оформления заказа его номер появляется в разделе В
работе

[test_personal_area.py]  
TestPersonalArea::test_transfer_to_personal_area_by_click - проверяет переход по клику в личный кабинет
TestPersonalArea::test_transfer_to_order_history - проверяет переход в раздел История заказов
TestPersonalArea::test_exit_button - проверяет выход из аккаунта
TestPersonalArea::test_login_user_can_make_order - проверяет, что залогиненный пользователь может оформить заказ

[test_restore_password.py]
TestRestorePassword::test_transfer_from_restore_button_to_restore_page - проверяет, что клик по кнопке «Восстановить
пароль» переводит на страницу запроса восстановления пароля
TestRestorePassword::test_input_email_click_restore_button - проверяет, что ввод почты и клик по кнопке «Восстановить»
переводит на страницу восстановления пароля
TestRestorePassword::test_show_hide_password_on_restore_page - проверяет, что клик по кнопке показать/скрыть пароль
делает поле активным — подсвечивает его
