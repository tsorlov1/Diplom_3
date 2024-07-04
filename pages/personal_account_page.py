import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Заполнение поля "Email"')
    def set_email_field(self, email):
        self.send_keys(PersonalAccountPageLocators.EMAIL_FIELD_LOGIN, email)

    @allure.step('Заполнение поля "Пароль"')
    def set_password_field(self, password):
        self.send_keys(PersonalAccountPageLocators.PASSWORD_FIELD_LOGIN, password)

    @allure.step('Нажать на кнопку "Войти"')
    def click_enter_button(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_ENTER)

    @allure.step('Ожидание загрузки главной страницы ')
    def wait_main_page(self):
        self.wait_for_visibility_of_element(PersonalAccountPageLocators.BUTTON_ORDER)

    @allure.step('Заполнение формы авторизации')
    def fill_form_login(self, url, email, password):
        self.open_url(url)
        self.set_email_field(email)
        self.set_password_field(password)
        self.click_enter_button()
        self.wait_main_page()

    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Ожидание загрузки страницы "Личный кабинет"')
    def wait_personal_account_page(self):
        self.wait_for_visibility_of_element(PersonalAccountPageLocators.BUTTON_PROFILE)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_order_history(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY)

    @allure.step('Ожидание загрузки страницы "История заказов"')
    def wait_order_history_page(self):
        self.wait_for_visibility_of_element(PersonalAccountPageLocators.ORDER_NUMBER_LAST_HISTORY)

    @allure.step('Получение номера последнего заказа в истории заказов')
    def get_order_number_history(self):
        current_text = self.get_current_text(PersonalAccountPageLocators.ORDER_NUMBER_LAST_HISTORY)
        return current_text

    @allure.step('Нажать на кнопку "Выход"')
    def click_exit_button(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_EXIT)

    @allure.step('Ожидание загрузки страницы авторизации')
    def wait_login_page(self):
        self.wait_for_visibility_of_element(PersonalAccountPageLocators.LOGIN_TITLE)



