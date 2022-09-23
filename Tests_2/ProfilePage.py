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
    companyname = (By.CSS_SELECTOR, "#organisationInput")
    companytype = (By.XPATH, "#my-profile > form > div:nth-child(7) > div.jsx-3705509386.col-md-5.col-lg-5.offset-md-2.col-xs-12.pl-0 > div > div.react-select-padding.css-2b097c-container > div > div.react-select-padding__value-container.css-1hwfws3 > div")
    companysize = (By.CSS_SELECTOR, "#my-profile > form > div:nth-child(8) > div:nth-child(1) > div > div.react-select-padding.css-2b097c-container > div > div.react-select-padding__value-container.css-1hwfws3 > div")
    industry = (By.CSS_SELECTOR, "#my-profile > form > div:nth-child(8) > div.jsx-3705509386.col-md-5.col-lg-5.offset-md-2.pl-0.col-xs-12 > div > div.react-select-padding.css-2b097c-container > div > div.react-select-padding__value-container.css-1hwfws3 > div")
    designation = (By.CSS_SELECTOR, "#my-profile > form > div:nth-child(9) > div:nth-child(1) > div > div.react-select-padding.css-2b097c-container > div > div.react-select-padding__value-container.react-select-padding__value-container--has-value.css-1hwfws3 > div > div > div")
    job_role = (By.CSS_SELECTOR, "#my-profile > form > div:nth-child(9) > div.jsx-3705509386.col-md-5.col-lg-5.offset-md-2.col-xs-12.pl-0 > div > div.react-select-padding.css-2b097c-container > div > div.react-select-padding__value-container.react-select-padding__value-container--has-value.css-1hwfws3 > div > div")
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

    def company_type(self):
        return self.driver.find_element(*ProfilePage.companytype).click()

    def company_size(self):
        return self.driver.find_element(*ProfilePage.companysize).click()

    def industry_name(self):
        return self.driver.find_element(*ProfilePage.industry).click()

    def designation_name(self):
        return self.driver.find_element(*ProfilePage.designation).click()

    def jobrole(self):
        return self.driver.find_element(*ProfilePage.job_role).click()

    def update_button(self):
        return self.driver.find_element(*ProfilePage.update).click()







