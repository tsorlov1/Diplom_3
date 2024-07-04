from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    EMAIL_FIELD_LOGIN = (By.NAME, "name")  # Поле "EMAIL" на странице авторизации
    PASSWORD_FIELD_LOGIN = (By.NAME, "Пароль")  # Поле "Пароль" на странице авторизации
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Кнопка "Личный кабинет"
    BUTTON_PROFILE = (By.XPATH, '//a[text()="Профиль"]')  # Кнопка "Профиль"
    BUTTON_ORDER_HISTORY = (By.XPATH, '//a[text()="История заказов"]')  # кнопка "История заказов"
    ORDER_NUMBER_LAST_HISTORY = (By.XPATH, "//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[last()]//p[1]")  # номер последнего заказа заказа в ленте и в истории

    BUTTON_EXIT = (By.XPATH, '//button[text()="Выход"]')  # Кнопка "Выход"
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")  # Заголовок "Вход"
