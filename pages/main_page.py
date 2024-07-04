import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажать на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Ожидание загрузки страницы "Конструктор"')
    def wait_constructor_page(self):
        self.wait_for_visibility_of_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_orders_feed_button(self):
        self.click_element(MainPageLocators.BUTTON_ORDERS_FEED)

    @allure.step('Ожидание загрузки страницы "Лента заказов"')
    def wait_orders_feed_page(self):
        self.wait_for_visibility_of_element(MainPageLocators.ORDER_FEED_TITLE)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_main_page(self):
        self.wait_for_visibility_of_element(MainPageLocators.BUTTON_LOGIN_ACCOUNT)

    @allure.step('Нажать на кнопку "Ингредиент"')
    def click_ingredient_button(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def check_ingredient_details_window(self):
        assert self.get_current_text(MainPageLocators.DETAILS_WINDOW_TITLE) == 'Детали ингредиента'

    @allure.step('Нажать на крестик для закрытия окна с деталями ингредиента')
    def click_close_ingredient_details_window(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUTTON_CLOSE_WINDOW)
        self.click_element(MainPageLocators.BUTTON_CLOSE_WINDOW)

    @allure.step('Проверка: всплывающее окно с деталями ингредиента закрыто')
    def check_close_ingredient_details_window(self):
        assert self.wait_invisibility_of_element(MainPageLocators.DETAILS_WINDOW_TITLE)

    @allure.step('Получение значения счетчика ингредиента')
    def get_ingredient_counter(self):
        return self.get_current_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredients_order(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.BASKET)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_element(MainPageLocators.BUTTON_ORDER)

    @allure.step('Проверка: открылось окно с деталями заказа')
    def check_order_window(self):
        assert self.wait_for_visibility_of_element(MainPageLocators.ORDER_WINDOW).is_displayed()

    @allure.step('Нажать на крестик для закрытия окна с деталями заказа')
    def click_close_order_details_window(self):
        self.get_order_number()
        self.click_element(MainPageLocators.BUTTON_CLOSE_WINDOW)

    @allure.step('Создание заказа')
    def make_order(self):
        self.add_ingredients_order()
        self.click_order_button()
        self.click_close_order_details_window()

    @allure.step('Получение номера заказа в всплывающем окне после оформления заказа')
    def get_order_number(self):
        while True:
            element = self.wait_for_visibility_of_element(MainPageLocators.ORDER_NUMBER)
            a = element.text
            if a != "9999":
                break
        return element.text
