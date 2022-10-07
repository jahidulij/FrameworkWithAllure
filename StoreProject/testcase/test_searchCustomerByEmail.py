import string
import random
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from StoreProject.pageObjects.AddCustomerPage import AddCustomer
from StoreProject.pageObjects.SearchCustomer import SearchCustomer
from StoreProject.pageObjects.LoginPage import LoginPage
from StoreProject.utilities.customLogger import customLogger
from StoreProject.utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = customLogger()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup1):
        self.logger.info("**** Test_004_SearchCustomerByEmail ****")
        self.driver = setup1
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**** Login Successful ****")

        self.logger.info("**** Starting Search customer Test ****")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickOnCustomerMenu()
        self.addCustomer.clickOnCustomerSubMenu()

        self.searchCustomer = SearchCustomer(self.driver)

        self.logger.info("**** Providing Customer Search Info ****")
        self.searchCustomer.setSearchEmail("james_pan@nopCommerce.com")
        self.searchCustomer.clickOnSearch()

        nop = self.driver.find_element(By.XPATH, "//b[contains(text(),'nopCommerce version 4.50.0')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", nop)
        time.sleep(3)

        res_email = self.searchCustomer.verifyEmailSearchResult()
        if "james_pan@nopCommerce.com" in res_email:
            assert True
            self.logger.info("**** Customer found ****")
            self.logger.info("**** Test_004_SearchCustomerByEmail finished ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:/Users/JahidulIslam/PycharmProjects/pytestSeleniumEasy2/StoreProject/screenshots/test_searchCustomerByEmail.png")
            self.logger.error("**** Customer not found ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_searchCustomerByEmail",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
