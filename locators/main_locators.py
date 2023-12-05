from selenium.webdriver.common.by import By


class MainLocators:

    CONSTRUCT_LINK = (By.XPATH, ".//p[text()='Конструктор']")
    CONSTRUCTOR = (By.XPATH, ".//h1[text()='Соберите бургер']")

    ORDER_LINE_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    ORDER_LINE = (By.XPATH, ".//div[@class='OrderFeed_contentBox__3-tWb']")
    ORDER_LINE_ELEMENT_BUN = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    ORDER_BUN_COUNTER = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[@class='counter_counter__num__3nue1']")
    ORDER_ELEMENT_DETAILS_POP_UP = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")

    ORDER_LINE_ELEMENT_SAUCE = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    ORDER_SAUCE_COUNTER = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//p[@class='counter_counter__num__3nue1']")

    ORDER = (By.XPATH, ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")
    ORDER_IN_ORDER_LINE = (By.XPATH, ".//a[@class='OrderHistory_link__1iNby']")
    ORDER_DETAILS_POP_UP = (By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    ORDER_IN_WORK = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")

    CLOSE_DETAILS_BUTTON = (
    By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    MADE_ORDER_POP_UP = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")
    MADE_ORDER_POP_UP_NUMBER = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']/h2")
    MADE_ORDER_IN_ORDER_LINE = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']/p[@class='text text_type_digits-default']")

    ALLTIME_ORDER_COUNTER = (By.XPATH, ".//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    DAILY_ORDER_COUNTER = (By.XPATH, ".//div/p[text()='Выполнено за сегодня:']/../p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
