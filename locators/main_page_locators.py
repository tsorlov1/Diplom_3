from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # заголовок в конструкторе "Соберите бургер"
    ORDER_FEED_TITLE = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']")  # заголовок Лента заказов
    BUTTON_ORDERS_FEED = (By.XPATH, "//p[text()='Лента Заказов']")  # кнопка "Лента заказов"
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    INGREDIENT = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")  # ингредиент
    DETAILS_WINDOW_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # заголовок окна с деталями об ингредиенте
    BUTTON_CLOSE_WINDOW = (By.XPATH, "//button[@type='button']")  # кнопка крестик в окне с деталями об ингредиенте
    BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")  # корзина конструктора
    INGREDIENT_COUNTER = (By.XPATH, "//ul[1]/a[1]//p[contains(@class, 'num')]")  # счетчик ингредиента
    BUTTON_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка "Оформить заказ"
    ORDER_WINDOW = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']")  # окно после оформления заказа
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')  # номер заказа в окне после создания
