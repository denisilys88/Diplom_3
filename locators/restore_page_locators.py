from selenium.webdriver.common.by import By


class RestorePageLocators:

    RESTORE_PASS_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    RESTORE_MAIL_FIELD = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")
    RESTORE_MAIL_FIELD_ACTIVE = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='text']")
    SHOW_SIGN = (By.XPATH, ".//div[@class='input__icon input__icon-action']")
