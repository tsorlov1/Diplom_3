import faker


class User:
    @staticmethod
    def user_random():
        fake = faker.Faker()
        user_data_random = {
            'email': fake.email(),
            'password': fake.password(),
            'name': fake.name()
        }
        return user_data_random

class Url:
    URL_BASE = 'https://stellarburgers.nomoreparties.site/'
    URL_FORGOT_PASSWORD = f'{URL_BASE}forgot-password'
    URL_LOGIN = f'{URL_BASE}login'
    URL_RESET_PASSWORD = f'{URL_BASE}reset-password'
    URL_PROFILE = f'{URL_BASE}account/profile'
    URL_ORDER_HISTORY = f'{URL_BASE}account/order-history'
    URL_ORDERS_FEED = f'{URL_BASE}feed'

class ApiUrl:
    API_URL_CREATE_USER = f'{Url.URL_BASE}api/auth/register'
    API_URL_LOGIN_USER = f'{Url.URL_BASE}api/auth/login'
    API_URL_DELETE_USER = f'{Url.URL_BASE}api/auth/user'

EMAIL = 'korneeva2506@gmail.com'
PASSWORD = '123456'
