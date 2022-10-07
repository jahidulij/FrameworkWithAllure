import time
import allure
import pytest
from allure_commons.types import AttachmentType

from StoreProject.utilities.readProperties import ReadConfig
from StoreProject.pageObjects import LoginPage
from StoreProject.utilities.customLogger import customLogger
from StoreProject.utilities import XLUtils

class Test_001_DDT_Login:
    base_url = ReadConfig.getApplicationURL()
    path = "C:/Users/JahidulIslam/PycharmProjects/pytestSeleniumEasy2/StoreProject/data/LoginData.xlsx"

    logger = customLogger()

    @pytest.mark.regression
    def test_login_ddt(self, setup1):
        self.logger.info("**** Test_001_DDT_Login ****")
        self.logger.info("**** Verifying Login Test ****")
        self.driver = setup1
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        self.lp = LoginPage.LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")

        list_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setEmail(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Passed ****")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed ****")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif actual_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Failed ****")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Passed ****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("**** Login DDT test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_ddt",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

        self.logger.info("**** End of Login DDT Test ****")
        self.logger.info("**** Completed Test_001_DDT_Login ****")
