import string
import random
import time
import allure
import pytest
from allure_commons.types import AttachmentType

from StoreProject.pageObjects.AddCustomerPage import AddCustomer
from StoreProject.pageObjects.LoginPage import LoginPage
from StoreProject.utilities.customLogger import customLogger
from StoreProject.utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger = customLogger()

    @pytest.mark.sanity
    def test_addCustomer(self, setup1):
        self.logger.info("**** Test_003_AddCustomer ****")
        self.driver = setup1
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**** Login Successful ****")

        self.logger.info("**** Starting Add Customer Test ****")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickOnCustomerMenu()
        self.addCustomer.clickOnCustomerSubMenu()
        self.addCustomer.clickOnAddNew()

        letters = string.ascii_lowercase
        mail = ''.join(random.choice(letters) for i in range(10))
        gmail = mail + "@gmail.com"
        self.username = gmail

        self.logger.info("**** Providing Customer Info ****")

        self.addCustomer.setEmail(self.username)
        self.addCustomer.setPassword("tet123")
        self.addCustomer.setFirstName("John")
        self.addCustomer.setLastName("Doe")
        self.addCustomer.setGender("Female")
        self.addCustomer.setDOB("9/30/2022")
        self.addCustomer.setCompanyName("ABC Test Inc")
        self.addCustomer.clickOnIsTaxExempt()
        # self.addCustomer.setNewsletter("Test store 2")
        # self.addCustomer.setCustomerRoles("Administrators")
        self.addCustomer.setManagerOfVendor("Vendor 1")
        self.addCustomer.clickOnActive()
        self.addCustomer.setAdminComment("Test comment")
        self.addCustomer.clickOnSave()
        time.sleep(3)

        # actual_title = driver.title
        # if actual_title == "Swag Labs":
        #     assert True
        # else:
        #     allure.attach(driver.get_screenshot_as_png(), name="test_01_login", attachment_type=AttachmentType.PNG)
        #     assert False

        message = self.addCustomer.verifySuccessMessage()
        print(message)
        if "customer has been added successfully." in message:
            assert True
            self.logger.info("**** Customer created successfully ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:/Users/JahidulIslam/PycharmProjects/pytestSeleniumEasy2/StoreProject/screenshots/test_addCustomer.png")
            self.logger.error("**** Customer not created ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_addCustomer", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
