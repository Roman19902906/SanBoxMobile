import time
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class MobilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

        # Страничка регистрации
        self.title = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgRegContent')

        # Поле ввода номера телефона
        self.field_number = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/etRegMask')

        # Ввод номера телефона
        self.enter_number = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgPhone')

        # Кнопка поля дня рождения
        self.enter_birthday = lambda: self.driver.find_element_by_id('biz.growapp.winline:id/vgBirthday')

        # Кнопка "ok" выбора дня рождения
        self.button_ok = lambda: self.driver.find_element_by_id('android:id/button1')

        # Поле ввода пароля
        self.enter_password = lambda: self.driver.find_element_by_id("biz.growapp.winline:id/etReg")

        # Поле ввода промо кода
        self.feild_promo = lambda: self.driver.find_element_by_id("biz.growapp.winline:id/vgHavePromoCode")

        # Ввод промо кода
        self.enter_promo = lambda: self.driver.find_element_by_xpath(
            "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText")

        # Чек-бокс согласия с правилами
        self.confirm_18_y_o = lambda: self.driver.find_element_by_id("biz.growapp.winline:id/vgAgreement")

        # Кнопка регистрации
        self.button_reg = lambda: self.driver.find_element_by_id("biz.growapp.winline:id/btnGetSmsCode")

        # Поле ввода sms
        self.feild_sms = lambda: self.driver.find_element_by_xpath(
            "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText")

        # Кнопка продолжить регистрацию
        self.button_continue_reg = lambda: self.driver.find_element(By.ID, "biz.growapp.winline:id/btnRegister")

        # Текст с ошибкой
        self.error_sms_text = lambda: self.wait_short.until(EC.presence_of_element_located(
            (By.XPATH,
             "//android.widget.FrameLayout[@resource-id='biz.growapp.winline:id/vgSmsCodeField']/android.widget.FrameLayout/android.widget.TextView[@resource-id='biz.growapp.winline:id/tvReg']")))

    @allure.step('Ожидание страницы регистрации')
    def wait_title(self):
        self.wait_short.until((EC.element_to_be_clickable(
            (By.ID, ("biz.growapp.winline:id/vgRegContent")))))
        self.title().click()
        return self

    @allure.step('Ввод номера телефона')
    def enter_number_phone(self):
        self.wait_short.until((EC.element_to_be_clickable(
            (By.ID, ("biz.growapp.winline:id/etReg")))))
        self.enter_number().click()
        self.field_number().send_keys('9999999999')
        return self

    @allure.step('Ввод номера телефона')
    def enter_birthday_date(self):
        self.enter_birthday().click()
        self.wait_short.until((EC.element_to_be_clickable(
            (By.ID, ("android:id/button1")))))
        self.button_ok().click()
        return self

    @allure.step('Ввод пароля')
    def enter_passwords(self):
        self.enter_password().send_keys('abc1234')
        return self

    @allure.step('Ввод промокода')
    def enter_promos(self):
        self.feild_promo().click()
        self.enter_promo().send_keys('123')
        return self

    @allure.step('Чек-бокс принятия условий')
    def enter_chek_box(self):
        self.confirm_18_y_o().click()
        return self

    @allure.step('Регистрация')
    def enter_button_reg(self):
        self.button_reg().click()
        return self

    @allure.step('Регистрация')
    def enter_password_sms(self):
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, (
                "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText")))))
        self.feild_sms().set_value('123456')
        return self

    def remove_keyboard(self):
        """ Спраятать клавиатуру """
        self.driver.hide_keyboard()
        return self

    @allure.step('Продолжить регистрацию')
    def enter_button_continue(self):
        self.button_continue_reg().click()
        time.sleep(10)
        return self

    def check_error_text(self):
        self.is_element_present(self.error_sms_text())
        return self
