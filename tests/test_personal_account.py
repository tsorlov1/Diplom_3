import allure
from data import Url, EMAIL, PASSWORD
from pages.personal_account_page import PersonalAccountPage


@allure.feature('Проверка «Личный кабинет»')
class TestPersonalAccount:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_personal_account_transition(self, driver):
        page = PersonalAccountPage(driver)
        page.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        page.click_personal_account_button()
        page.wait_personal_account_page()
        assert page.get_current_url() == Url.URL_PROFILE

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_order_history_transition(self, driver):
        page = PersonalAccountPage(driver)
        page.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        page.click_personal_account_button()
        page.wait_personal_account_page()
        page.click_order_history()
        page.wait_order_history_page()
        assert page.get_current_url() == Url.URL_ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_account(self, driver):
        page = PersonalAccountPage(driver)
        page.fill_form_login(Url.URL_LOGIN, EMAIL, PASSWORD)
        page.click_personal_account_button()
        page.wait_personal_account_page()
        page.click_exit_button()
        page.wait_login_page()
        assert page.get_current_url() == Url.URL_LOGIN
