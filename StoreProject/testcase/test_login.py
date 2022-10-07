import pytest
import allure
from allure_commons.types import AttachmentType

from StoreProject.utilities.readProperties import ReadConfig
from StoreProject.pageObjects import LoginPage
from StoreProject.utilities.customLogger import customLogger


class Test_001_Login:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = customLogger()

    @pytest.mark.regression
    def test_homepageTitle(self, setup1):
        self.logger.info("**** Test_001_Login ****")
        self.logger.info("**** Verifying Homepage Title ****")
        self.driver = setup1
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**** Homepage title test is passed ****")
        else:
            self.driver.save_screenshot(
                "C:/Users/JahidulIslam/PycharmProjects/pytestSeleniumEasy2/StoreProject/screenshots/test_homepageTitle.png")
            self.driver.close()
            self.logger.error("**** Homepage title test is failed ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_homepageTitle",
                          attachment_type=AttachmentType.PNG)
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup1):
        self.logger.info("**** Verifying Login Test ****")
        self.driver = setup1
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        self.lp = LoginPage.LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**** Login test is passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:/Users/JahidulIslam/PycharmProjects/pytestSeleniumEasy2/StoreProject/screenshots/test_login.png")
            self.driver.close()
            self.logger.error("**** Login test is failed ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login",
                          attachment_type=AttachmentType.PNG)
            assert False
