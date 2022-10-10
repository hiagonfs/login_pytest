from webbrowser import Chrome
import pytest
import json

@pytest.fixture(scope='session')
def config():
    with open('../config/config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture
def browser(config):
    if config['browser'] == 'chrome':
        driver = Chrome()
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    driver.implicitly_wait(config['wait_time'])
    yield driver
    driver.quit()
