from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    @property
    def wait_short(self):
        return WebDriverWait(self.driver, 15)

    def is_element_present(self, element):
        """Проверка наличия элемента"""
        try:
            element
        except NoSuchElementException:
            return False
        return True

    def element_is_not_present(self, element):
        """Проверка отсутсвия элемента"""
        try:
            element
        except NoSuchElementException:
            return True
        return False

