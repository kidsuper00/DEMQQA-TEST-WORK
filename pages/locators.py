from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthLocators:
    AUTH_NAME = (By.XPATH, '//*[@id="userName"]')
    AUTH_EMAIL = (By.XPATH, '//*[@id="userEmail"]')
    AUTH_CURRENT_ADDRESS = (By.XPATH, '//*[@id="currentAddress"]')
    AUTH_PERMANENT_ADDRESS = (By.XPATH, '//*[@id="permanentAddress"]')
    AUTH_SUBMITE = (By.XPATH, '//*[@id="submit"]')

    AUTH_NAME2 = (By.XPATH, '//*[@id="name"]')
    AUTH_EMAIL2 = (By.XPATH, '//*[@id="email"]')
    AUTH_CURRENT_ADDRESS2 = (By.XPATH, '//*[@id="output"]//*[contains(@id, "currentAddress")]')
    AUTH_PERMANENT_ADDRESS2 = (By.XPATH, '//*[@id="output"]//*[contains(@id, "permanentAddress")]')






