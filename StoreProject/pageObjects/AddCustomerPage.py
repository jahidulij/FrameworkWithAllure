import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomer:
    menu_customer_xpath = "//ul[@data-widget='treeview']/li/a[@class='nav-link']/p[contains(text(),'Customers')]"
    submenu_customer_xpath = "//ul/li[1]/a/p[contains(text(),' Customers')]"

    button_add_new_xpath = "//div[@class='float-right']/a"

    text_email_id = "Email"
    text_password_id = "Password"
    text_firstname_id = "FirstName"
    text_lastname_id = "LastName"
    radio_gender_male_id = "Gender_Male"
    radio_gender_female_id = "Gender_Female"
    date_bday_id = "DateOfBirth"
    text_company_name_id = "Company"
    checkbox_tax_exempt_id = "IsTaxExempt"

    dropdown_newsletter_xpath = "//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    multi_check_newsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    newsletter_your_store_xpath = "//span[contains(text(),'Your store name')]"
    newsletter_test_store_2_xpath = "//span[contains(text(),'Test store 2')]"

    customer_roles_xpath = "//select[@id='SelectedCustomerRoleIds']"
    multi_check_customer_role_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    customer_role_admin_xpath = "//span[contains(text(),'Administrators')]"
    customer_role_forum_moderator_xpath = "//span[contains(text(),'Forum Moderators')]"
    customer_role_guest_xpath = "//span[contains(text(),'Guests')]"
    customer_role_registered_xpath = "//span[contains(text(),'Registered')]"
    customer_role_vendors_xpath = "//span[contains(text(),'Vendors')]"

    dropdown_manager_of_vendor_id = "VendorId"

    checkbox_active_id = "Active"
    textarea_admin_comment_id = "AdminComment"
    button_save_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    # button_save_and_continue_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[2]"
    success_message = "//body/div[3]/div[1]/div[1]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.menu_customer_xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element(By.XPATH, self.submenu_customer_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.button_add_new_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element(By.ID, self.text_firstname_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.ID, self.text_lastname_id).send_keys(lastName)

    def setGender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.ID, self.radio_gender_male_id).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.ID, self.radio_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_gender_male_id).click()

    def setDOB(self, dob):
        self.driver.find_element(By.ID, self.date_bday_id).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.ID, self.text_company_name_id).send_keys(companyName)

    def clickOnIsTaxExempt(self):
        self.driver.find_element(By.ID, self.checkbox_tax_exempt_id).click()

    def setNewsletter(self, newsletterName):
        self.driver.find_element(By.XPATH, self.multi_check_newsletter_xpath).click()
        newsletter_dropdown = self.driver.find_element(By.XPATH, self.dropdown_newsletter_xpath)
        select = Select(self.wait.until(EC.presence_of_element_located(newsletter_dropdown)))
        # select.select_by_visible_text(newsletterName)
        select.select_by_value("2")

        # if newsletterName.lower() == "Your store name":
        #     self.driver.find_element(By.XPATH, self.newsletter_your_store_xpath).click()
        # elif newsletterName.lower() == "Test store 2":
        #     self.driver.find_element(By.XPATH, self.newsletter_test_store_2_xpath).click()
        # else:
        #     self.driver.find_element(By.XPATH, self.newsletter_your_store_xpath).click()

    def setCustomerRoles(self, role):
        customer_role = self.driver.find_element(By.XPATH, self.multi_check_customer_role_xpath)
        customer_role.click()
        customer_roles = self.driver.find_elements(By.XPATH, self.customer_roles_xpath)

        time.sleep(3)
        self.wait.until(EC.visibility_of_element_located(customer_roles))
        select = Select(customer_roles)
        select.select_by_visible_text(role)

        # self.driver.find_element(By.XPATH, self.multi_check_customer_role_xpath).click()
        # if role.lower() == "administrators":
        #     self.listitem = self.driver.find_element(By.XPATH, self.customer_role_admin_xpath)
        # elif role.lower() == "forum moderators":
        #     self.listitem = self.driver.find_element(By.XPATH, self.customer_role_forum_moderator_xpath)
        # elif role.lower() == "guests":
        #     self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
        #     self.listitem = self.driver.find_element(By.XPATH, self.customer_role_guest_xpath)
        # elif role.lower() == "registered":
        #     self.listitem = self.driver.find_element(By.XPATH, self.customer_role_registered_xpath)
        # elif role.lower() == "vendors":
        #     self.listitem = self.driver.find_element(By.ID, self.customer_role_vendors_xpath)
        # else:
        #     self.listitem = self.driver.find_element(By.XPATH, self.customer_role_guest_xpath)

        # time.sleep(2)
        # self.listitem.click()
        # self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, vendor):
        manager_of_vendor = self.driver.find_element(By.ID, self.dropdown_manager_of_vendor_id)
        select = Select(manager_of_vendor)
        select.select_by_visible_text(vendor)

    def clickOnActive(self):
        self.driver.find_element(By.ID, self.checkbox_active_id).click()

    def setAdminComment(self, comment):
        self.driver.find_element(By.ID, self.textarea_admin_comment_id).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def verifySuccessMessage(self):
        self.message = self.driver.find_element(By.XPATH, self.success_message)
        actual_message = self.message.text
        return actual_message
