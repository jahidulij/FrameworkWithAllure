from selenium.webdriver.common.by import By

class SearchCustomer:
    search_email_id = "SearchEmail"
    text_firstname_id = "SearchFirstName"
    text_lastname_id = "SearchLastName"
    button_search_id = "search-customers"
    result_email_xpath = "//tr[@class='odd']/td[2]"
    result_name_xpath = "//tr[@class='odd']/td[3]"

    def __init__(self, driver):
        self.driver = driver

    def setSearchEmail(self, email):
        self.mail = self.driver.find_element(By.ID, self.search_email_id)
        self.mail.clear()
        self.mail.send_keys(email)

    def setFirstName(self, fname):
        self.name = self.driver.find_element(By.ID, self.text_firstname_id)
        self.name.clear()
        self.name.send_keys(fname)

    def setLastName(self, lname):
        self.name = self.driver.find_element(By.ID, self.text_lastname_id)
        self.name.clear()
        self.name.send_keys(lname)

    def clickOnSearch(self):
        self.driver.find_element(By.ID, self.button_search_id).click()

    def verifyEmailSearchResult(self):
        result_email = self.driver.find_element(By.XPATH, self.result_email_xpath).text
        return result_email

    def verifyNameSearchResult(self):
        name = self.driver.find_element(By.XPATH, self.result_name_xpath).text
        return name
