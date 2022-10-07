import time
import pytest
import allure
from allure_commons.types import AttachmentType

from StoreProject.pageObjects.AddCustomerPage import AddCustomer
from StoreProject.pageObjects.OnlineCustomerListDDT import OnlineCustomerListDDT
from StoreProject.pageObjects.LoginPage import LoginPage
from StoreProject.utilities.customLogger import customLogger
from StoreProject.utilities.readProperties import ReadConfig


class Test_007_GetOnlineCustomersListDDT:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = customLogger()

    @pytest.mark.skip
    @pytest.mark.regression
    def test_onlineCustomeListDDT(self, setup1):
        self.logger.info("**** Test_007_GetOnlineCustomersListDDT ****")
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

        self.onlineCustomerListDDT = OnlineCustomerListDDT(self.driver)
        self.onlineCustomerListDDT.clickOnOnlineCustomers()
        self.onlineCustomerListDDT.getClientHeaderInfo()
        # self.onlineCustomerListDDT.getClientTableInfo()

        time.sleep(3)

        res_name = self.onlineCustomerListDDT.verifyHeaderContent()
        if "Customer info" in res_name:
            assert True
            self.logger.info("**** Header matched ****")
            self.logger.info("**** Test_007_GetOnlineCustomersListDDT finished ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:/Users/JahidulIslam/PycharmProjects/pytestSeleniumEasy2/StoreProject/screenshots/test_onlineCustomeListDDT.png")
            self.logger.error("**** Header not matched ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_onlineCustomeListDDT",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
