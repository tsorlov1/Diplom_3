import pytest
from selenium import webdriver
import requests
from data import Url, ApiUrl, User


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Url.URL_BASE)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(Url.URL_BASE)
    yield driver
    driver.quit()

@pytest.fixture
def registration_user_random(driver):
    payload = User.user_random()
    response = requests.post(ApiUrl.API_URL_CREATE_USER, json=payload)
    token = response.json().get('accessToken')
    yield payload, token

    headers = {'Authorization': f'Bearer {token}'}
    requests.delete(ApiUrl.API_URL_DELETE_USER, headers=headers)

@pytest.fixture
def login(driver, user_registration):
    payload, token = user_registration
    email = payload["email"]
    password = payload["password"]
    main_page = MainPage(driver)
    main_page.click_on_personal_account()
    login_page = LoginPage(driver)
    login_page.login(email, password)
    return driver


