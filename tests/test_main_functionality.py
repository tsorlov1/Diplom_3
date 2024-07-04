import allure
from data import Url, EMAIL, PASSWORD
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage


@allure.feature('Проверка «Личный кабинет»')
class TestMainFunctionality:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_constructor_transition(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        personal_account_page.click_personal_account_button()
        personal_account_page.wait_personal_account_page()
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        main_page.wait_constructor_page()
        assert main_page.get_current_url() == Url.URL_BASE

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_orders_feed_transition(self, driver):
        main_page = MainPage(driver)
        main_page.click_orders_feed_button()
        main_page.wait_orders_feed_page()
        assert main_page.get_current_url() == Url.URL_ORDERS_FEED

    @allure.title('Проверка: если кликнуть на ингредиент, появляется всплывающее окно с деталями')
    def test_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_button()
        main_page.check_ingredient_details_window()

    @allure.title('Проверка: всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_button()
        main_page.click_close_ingredient_details_window()
        main_page.check_close_ingredient_details_window()

    @allure.title('Проверка: при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_add_ingredient_order(self, driver):
        main_page = MainPage(driver)
        before_add_ingredient = main_page.get_ingredient_counter()
        main_page.add_ingredients_order()
        after_add_ingredient = main_page.get_ingredient_counter()
        assert after_add_ingredient > before_add_ingredient

    @allure.title('Проверка: залогиненный пользователь может оформить заказ')
    def test_make_order_login_user(self, driver):
        page_personal_account = PersonalAccountPage(driver)
        page_personal_account.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        main_page = MainPage(driver)
        main_page.add_ingredients_order()
        main_page.click_order_button()
        main_page.check_order_window()
