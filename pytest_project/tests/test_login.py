from selenium import webdriver
from pages.login import LoginPage
from data.auth import Auth
import logging
from conftest import browser

LOGGER = logging.getLogger(__name__)

login = LoginPage(browser)
auth = Auth()


def test_initial_page():
    LOGGER.info('acess the initial page')
    login.load()


def test_insert_email():
    LOGGER.info('insert email')
    email = auth.get_email()
    LOGGER.info('this e-mail is: ' + email)
    login.write_email(email)


def test_insert_password():
    LOGGER.info('insert email')
    password = auth.get_password()
    LOGGER.info('this password is: ' + password)
    login.write_password(password)


def test_click_button():
    LOGGER.info('click in button')
    login.click_button()


def test_home_page():
    LOGGER.info('logged in home page')
    assert True
