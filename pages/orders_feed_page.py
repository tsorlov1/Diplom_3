import allure
from locators.orders_feed_locators import OrdersFeedPageLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    @allure.step('Нажать на карточку заказа в Ленте заказов')
    def click_order_card(self):
        self.click_element(OrdersFeedPageLocators.ORDER_CARD)

    @allure.step('Проверка: по нажатии на карточку заказа открылось окно с деталями о заказе')
    def check_order_details_window(self):
        assert self.wait_for_visibility_of_element(OrdersFeedPageLocators.ORDER_DETAILS_WINDOW).is_displayed()

    @allure.step('Получение значения счетчика "Выполнено за сегодня"')
    def get_count_day(self):
        return self.get_current_text(OrdersFeedPageLocators.DAY_COUNTER)

    @allure.step('Получение значения счетчика "Выполнено за всё время"')
    def get_count_all_time(self):
        return self.get_current_text(OrdersFeedPageLocators.ALL_TIME_COUNTER)

    @allure.step('Получение текущего номера заказа в разделе "В работе"')
    def get_order_section_in_work(self):
        return self.get_current_text(OrdersFeedPageLocators.SECTION_IN_WORK)

    @allure.step('Получение номера последнего заказа в Ленте заказов')
    def get_order_number_feed(self):
        current_text = self.get_current_text(OrdersFeedPageLocators.ORDER_NUMBER_LAST_FEED)
        return current_text






