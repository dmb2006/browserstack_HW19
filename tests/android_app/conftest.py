import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser
import os
from appium import webdriver

from until import attach


@pytest.fixture(scope="function", autouse=True)
def android_management():
    load_dotenv()

    username = os.getenv('BS_USERNAME')
    access_key = os.getenv('BS_ACCESS_KEY')

    if not username or not access_key:
        raise ValueError(
            'Не заданы BS_USERNAME или BS_ACCESS_KEY в файле .env'
        )

    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Ultra",
        "app": "bs://sample.app",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": username,
            "accessKey": access_key
        }
    })

    driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.timeout = float(os.getenv('SELENE_TIMEOUT', '10.0'))

    yield browser

    session_id = browser.driver.session_id
    attach.add_screenshot()
    attach.add_xml()
    attach.add_video(session_id, username, access_key)


    browser.quit()
