import allure
from data import Url, EMAIL
from pages.password_recovery_page import PasswordRecoveryPage


@allure.feature('Проверка «Восстановление пароля»')
class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recovery_page_transition(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open_url(Url.URL_LOGIN)
        page.click_button_password_recovery()
        assert page.get_current_url() == Url.URL_FORGOT_PASSWORD

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_recovery_page_set_email_click_button_recovery(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open_url(Url.URL_LOGIN)
        page.click_button_password_recovery()
        page.set_email_field(EMAIL)
        page.click_button_recovery()
        page.wait_password_recovery_page()
        assert page.get_current_url() == Url.URL_RESET_PASSWORD

    @allure.title('Проверка активации поля по нажатии кнопки показать/скрыть пароль')
    def test_recovery_page_click_button_password_show(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open_url(Url.URL_LOGIN)
        page.click_button_password_recovery()
        page.set_email_field(EMAIL)
        page.click_button_recovery()
        page.wait_password_recovery_page()
        inactive_field_password = page.get_element_attribute()
        page.click_button_password_show()
        active_field_password = page.get_element_attribute()
        assert inactive_field_password != active_field_password
