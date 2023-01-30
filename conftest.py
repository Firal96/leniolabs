"""
This module contains shared fixture.
"""

import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)
    assert config['browser'] in ['Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
        opts.add_argument('--window-size=1920,1080')
        b = selenium.webdriver.Firefox(options=opts)
    elif config['browser'] == 'Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('--window-size=1920,1080')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported in local mode')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the instance
    b.quit
