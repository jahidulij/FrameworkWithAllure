import time

from selenium.webdriver.common.by import By


class LoginPage:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    button_logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
