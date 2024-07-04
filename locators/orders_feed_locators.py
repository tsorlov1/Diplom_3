from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:

    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")  # карточка заказа в Ленте заказов
    ORDER_DETAILS_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")  # окно с деталями о заказе
    DAY_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")  # счетчик закзов за день
    ALL_TIME_COUNTER = (By.XPATH, "//div[@class='undefined mb-15']/p[2]")  # cчетчик заказов за все время
    SECTION_IN_WORK = (By.XPATH, f"//li[contains(text(), '0')]")  # раздел "В работе"
    ORDER_NUMBER_LAST_FEED = (By.XPATH, "//li//p[@class='text text_type_digits-default']")  # номер последнего заказа заказа в ленте заказов
