from selenium.webdriver.common.by import By


class RegistratonPage:
    URL = 'https://www.facebook.com/'
    SEARCH_FIRST_NAME = (By.NAME, 'firstname')
    SEARCH_LAST_NAME = (By.NAME, 'lastname')
    SEARCH_EMAIL = (By.NAME, 'reg_email__')
    SEARCH_PASSWORD = (By.NAME, 'reg_passwd__')
    SEX_FEMALE = (By.ID, 'u_3_4_VZ')
    SEX_MALE = (By.ID, 'u_3_5_uz')
    SEX_OTHER = (By.ID, 'u_3_6_Tr')
    BUTTON_REGISTER = (By.NAME, 'websubmit')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def write_first_name(self, name):
        search_input = self.browser.find_element(*self.SEARCH_FIRST_NAME)
        search_input.send_keys(name)

    def write_last_name(self, name):
        search_input = self.browser.find_element(*self.SEARCH_LAST_NAME)
        search_input.send_keys(name)

    def write_email(self, email):
        search_input = self.browser.find_element(*self.SEARCH_EMAIL)
        search_input.send_keys(email)

    def write_password(self, password):
        search_input = self.browser.find_element(*self.SEARCH_PASSWORD)
        search_input.send_keys(password)

    def click_sex_female(self):
        self.SEX_FEMALE.click()

    def click_sex_male(self):
        self.SEX_MALE.click()

    def click_sex_other(self):
        self.SEX_OTHER.click()

    def click_button(self):
        self.BUTTON_LOGIN.click()
