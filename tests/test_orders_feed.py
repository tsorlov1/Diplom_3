import allure
from data import Url, EMAIL, PASSWORD
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage


@allure.feature('Проверка раздела «Лента заказов»')
class TestOrdersFeed:
    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_card(self, driver):
        main_page = MainPage(driver)
        main_page.click_orders_feed_button()
        main_page.wait_orders_feed_page()
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.click_order_card()
        orders_feed_page.check_order_details_window()


    @allure.title('Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_number_history_orders_in_orders_feed(self, driver):
        page_personal_account = PersonalAccountPage(driver)
        page_personal_account.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        main_page = MainPage(driver)
        main_page.make_order()
        page_personal_account.click_personal_account_button()
        page_personal_account.wait_personal_account_page()
        page_personal_account.click_order_history()
        page_personal_account.wait_order_history_page()
        order_number_history = page_personal_account.get_order_number_history()
        main_page.click_orders_feed_button()
        orders_feed_page = OrdersFeedPage(driver)
        order_number_feed = orders_feed_page.get_order_number_feed()
        assert order_number_history == order_number_feed

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за день увеличивается')
    def test_counter_day_increased_after_new_order(self, driver):
        page_personal_account = PersonalAccountPage(driver)
        page_personal_account.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        main_page = MainPage(driver)
        main_page.click_orders_feed_button()
        orders_feed_page = OrdersFeedPage(driver)
        count_day = int(orders_feed_page.get_count_day())
        main_page.click_constructor_button()
        main_page.make_order()
        main_page.click_orders_feed_button()
        count_day_updated = int(orders_feed_page.get_count_day())
        assert count_day_updated > count_day

    @allure.title('Проверка что при создании нового заказа счётчик Выполнено за все время увеличивается')
    def test_counter_all_time_increased_after_new_order(self, driver):
        page_personal_account = PersonalAccountPage(driver)
        page_personal_account.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        main_page = MainPage(driver)
        main_page.click_orders_feed_button()
        orders_feed_page = OrdersFeedPage(driver)
        count_day = int(orders_feed_page.get_count_all_time())
        main_page.click_constructor_button()
        main_page.make_order()
        main_page.click_orders_feed_button()
        count_day_updated = int(orders_feed_page.get_count_all_time())
        assert count_day_updated > count_day

    @allure.title('Проверка что после оформления заказа его номер появляется в разделе В работе')
    def test_order_number_in_section_in_work(self, driver):
        page_personal_account = PersonalAccountPage(driver)
        page_personal_account.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        main_page = MainPage(driver)
        main_page.add_ingredients_order()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        main_page.click_close_order_details_window()
        main_page.click_orders_feed_button()
        orders_feed_page = OrdersFeedPage(driver)
        order_number_in_work = orders_feed_page.get_order_section_in_work()
        assert int(order_number_in_work) == int(order_number)
