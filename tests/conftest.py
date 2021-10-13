import os
from selenium import webdriver
import allure
import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def init_mobile_device():
    desired_caps = {"platformName": "Android",
    "appium:platformVersion": "10.0",
    "appium:appPackage": "biz.growapp.winline",
    "appium:appActivity": "biz.growapp.winline.presentation.splash.SplashActivity"}
    driver = webdriver.Remote('http://127.0.0.2:4723/wd/hub', desired_capabilities=desired_caps)
    print("\nstart browser..")
    yield driver
    print("\nquit browser..")
    driver.close_app()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))



