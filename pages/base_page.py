from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def wait_for_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 45).until(expected_conditions.visibility_of_element_located(locator))

    def wait_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))

    def open_url(self, url):
        open_url = self.driver.get(url)
        return open_url

    def get_attribute(self, locator):
        attribute = self.driver.find_element(*locator).get_attribute('type')
        return attribute

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_current_text(self, locator):
        current_text = self.wait_for_visibility_of_element(locator).text
        return current_text

    def drag_and_drop_element(self, locator_one, locator_two):
        draggable = WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator_one))
        droppable = WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator_two))
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()
