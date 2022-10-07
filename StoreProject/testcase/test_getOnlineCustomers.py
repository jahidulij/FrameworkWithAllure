import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from StoreProject.pageObjects.AddCustomerPage import AddCustomer
from StoreProject.pageObjects.OnlineCustomerList import OnlineCustomerList
from StoreProject.pageObjects.LoginPage import LoginPage
from StoreProject.utilities.customLogger import customLogger
from StoreProject.utilities.readProperties import ReadConfig


class Test_006_GetOnlineCustomersList:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = customLogger()

    @pytest.mark.regression
    def test_onlineCustomerList(self, setup1):
        self.logger.info("**** Test_006_GetOnlineCustomersList ****")
        self.driver = setup1
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**** Login Successful ****")

        self.logger.info("**** Start finding online customer list ****")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickOnCustomerMenu()

        self.onlineCustomerList = OnlineCustomerList(self.driver)
        self.onlineCustomerList.clickOnOnlineCustomers()
        self.onlineCustomerList.getClientHeaderInfo()
        self.onlineCustomerList.getClientTableInfo()

        time.sleep(3)

        res_name = self.onlineCustomerList.verifyHeaderContent()
        if "Customer info" in res_name:
            assert True
            self.logger.info("**** Header matched ****")
            self.logger.info("**** Test_006_GetOnlineCustomersList finished ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:/Users/JahidulIslam/PycharmProjects/pytestSeleniumEasy2/StoreProject/screenshots/test_onlineCustomeList.png")
            self.logger.error("**** Header not matched ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_onlineCustomerList", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
