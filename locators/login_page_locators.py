from selenium.webdriver.common.by import By


class LoginPageLocators:

    INPUT_MAIL = (By.XPATH, ".//label[text()='Email']/../input[@value]")
    INPUT_PASSWORD = (By.XPATH, ".//label[text()='Пароль']/../input[@value]")
    ENTER_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    PERSONAL_AREA_LINK = (By.XPATH, ".//a[@href='/account']")
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    PROFILE = (By.XPATH, ".//a[@href='/account/profile']")
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[@href='/account/order-history']")
    ORDER_HISTORY = (By.XPATH, ".//div[@class='OrderHistory_orderHistory__qy1VB']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
