import allure
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators


class PasswordRecoveryPage(BasePage):
    @allure.step('Нажать на кнопку "Восстановить пароль')
    def click_button_password_recovery(self):
        self.click_element(PasswordRecoveryPageLocators.BUTTON_PASSWORD_RECOVERY)

    @allure.step('Ожидание загрузки страницы "Восстановление пароля"')
    def wait_password_recovery_page(self):
        self.wait_for_visibility_of_element(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_TITLE)

    @allure.step('Заполнение поля "Email"')
    def set_email_field(self, email):
        self.send_keys(PasswordRecoveryPageLocators.EMAIL_FIELD, email)

    @allure.step('Нажать на кнопку "Восстановить')
    def click_button_recovery(self):
        self.click_element(PasswordRecoveryPageLocators.BUTTON_RECOVERY)

    @allure.step('Ожидание кнопки "Сохранить"')
    def wait_password_recovery_page(self):
        self.wait_for_visibility_of_element(PasswordRecoveryPageLocators.BUTTON_SAVE)

    @allure.step('Нажать на кнопку "Показать/скрыть пароль')
    def click_button_password_show(self):
        self.click_element(PasswordRecoveryPageLocators.BUTTON_PASSWORD_SHOW)

    @allure.step('Получить атрибут элемента')
    def get_element_attribute(self):
        element_attribute = self.get_attribute(PasswordRecoveryPageLocators.PASSWORD_NEW_FIELD)
        return element_attribute
