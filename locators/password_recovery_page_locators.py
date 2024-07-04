from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, "//a[text()='Восстановить пароль']")  # Кнопка "Восстановить пароль"
    BUTTON_RECOVERY = (By.XPATH, "//button[contains(text(),'Восстановить')]")  # Кнопка "Восстановить"
    PASSWORD_RECOVERY_TITLE = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")  # Заголовок "Восстановление пароля"
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')  # Поле "Email"
    BUTTON_SAVE = (By.XPATH, '//button[text()="Сохранить"]')  # Кнопка "Сохранить"
    BUTTON_PASSWORD_SHOW = (By.XPATH, "//div[@class='input__icon input__icon-action']")  # Кнопка "Показать/скрыть пароль"
    PASSWORD_NEW_FIELD = (By.XPATH, '//input[@name="Введите новый пароль"]')  # Поле "Пароль"
