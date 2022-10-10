from selenium.webdriver.common.by import By

class LoginPage:

    URL = 'https://www.facebook.com/'
    SEARCH_EMAIL = (By.ID, 'email')
    SEARCH_PASSWORD = (By.ID, 'pass')
    BUTTON_LOGIN = (By.NAME, 'login')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def write_email(self, email):
        search_input = self.browser.find_element(*self.SEARCH_EMAIL)
        search_input.send_keys(email)

    def write_password(self, password):
        search_input = self.browser.find_element(*self.SEARCH_PASSWORD)
        search_input.send_keys(password)

    def click_button(self):
        self.BUTTON_LOGIN.click()
