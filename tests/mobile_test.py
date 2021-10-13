from sandbox.pages.mobile_page import MobilePage
import allure


@allure.epic('Проверки графика')
class TestMobile:
    @allure.story('Проверка даты')
    def test_date(self, init_mobile_device):
        mobile_page = MobilePage(init_mobile_device)
        mobile_page \
            .wait_title()\
            .enter_number_phone()\
            .enter_birthday_date()\
            .enter_passwords()\
            .enter_promos()\
            .enter_chek_box()\
            .enter_button_reg()\
            .enter_password_sms() \
            .remove_keyboard()\
            .enter_button_continue() \
            .check_error_text()