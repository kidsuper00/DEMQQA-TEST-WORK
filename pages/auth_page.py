from pages.base_page import BasePage
from pages.locators import AuthLocators
import time, os


class AuthPage(BasePage):

    def __init__(self, driver, url="https://demoqa.com/text-box"):
        self.driver = driver
        self.url = url
        super().__init__(self.driver, url=self.url)

    def open_auth_page(self):
        self.driver.get(self.url)
    def enter_name(self, fullname):
        name = self.driver.find_element(*AuthLocators.AUTH_NAME)
        name.send_keys(fullname)
        time.sleep(1)
    def enter_email(self, value):
        phone = self.driver.find_element(*AuthLocators.AUTH_EMAIL)
        phone.send_keys(value)

    def enter_current_address(self, value):
        phone = self.driver.find_element(*AuthLocators.AUTH_CURRENT_ADDRESS)
        phone.send_keys(value)

    def enter_permanent_address(self, value):
        phone = self.driver.find_element(*AuthLocators.AUTH_PERMANENT_ADDRESS)
        phone.send_keys(value)

    def btn_click(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_SUBMITE)
        btn.click()

    def get_result_data(self) -> tuple:
        name = self.driver.find_element(*AuthLocators.AUTH_NAME2).text
        email = self.driver.find_element(*AuthLocators.AUTH_EMAIL2).text
        current_address = self.driver.find_element(*AuthLocators.AUTH_CURRENT_ADDRESS2).text
        permanent_address = self.driver.find_element(*AuthLocators.AUTH_PERMANENT_ADDRESS2).text
        return name.replace("Name:",''), email.replace("Email:",''), current_address.replace("Current Address :",''), permanent_address.replace("Permananet Address :",'')
