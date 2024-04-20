from conftest import web_driver
from pages.auth_page import AuthPage
import time

name = "Aleksei Iakovlev"
email = "asa@mail.asa"
current_address = "Pushkina"
permanent_address = "QA-street"

def test_auth_page(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    page.enter_name(name)
    page.enter_email(email)
    page.enter_current_address(current_address)
    page.enter_permanent_address(permanent_address)
    page.btn_click()
    # time.sleep(3)
    name_result, email_result, current_address_result, permanent_address_result = page.get_result_data()
    assert name == name_result
    assert email == email_result
    assert current_address == current_address_result
    assert permanent_address == permanent_address_result
