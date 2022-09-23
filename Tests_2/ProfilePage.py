import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Tests_2.conftest import driver


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver

    FirstName = (By.NAME, "firstName")
    LastName = (By.ID, "nameInput")
    PhoneNumber = (By.ID, "phoneNumberInput")
    postalcode = (By.ID, "postalCodeInput")
    companyname = (By.ID, "organisationInput")
    companytype = (By.ID, "react-select-4-input")
    companysize = (By.ID, "react-select-5-input")
    industry = (By.ID, "react-select-6-input")
    job_role = (By.CSS_SELECTOR, "#react-select-17-input")
    update = (By.CSS_SELECTOR, "//button[@class='jsx-3705509386 btn btn-orange m-3 float-end']")

    def First_name(self):
        return self.driver.find_element(*ProfilePage.FirstName).send_keys("sansa")

    def Last_name(self):
        return self.driver.find_element(*ProfilePage.LastName).send_keys("stark")

    def ph_num(self):
        return self.driver.find_element(*ProfilePage.PhoneNumber).send_keys("9866765921")

    def post_code(self):
        return self.driver.find_element(*ProfilePage.postalcode).send_keys("535128")

    def company_name(self):
        return self.driver.find_element(*ProfilePage.companyname).send_keys("WIPRO")

    def update_button(self):
        return self.driver.find_element(*ProfilePage.update).click()







