import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

from Tests_2.LandingPage import LandingPage
from Tests_2.conftest import driver


class SigninPage:

    def __init__(self, driver):
        self.driver = driver

    cookies = (By.XPATH, "/html/body/div/div[3]/div/div/div[2]/div/button")
    email = (By.CSS_SELECTOR, "#__next > div.content-container.signedout > div.container-fluid.h-100 > div > div.col-lg-9.d-none.d-lg-block.py-5.bg-white > div > div > div > form > div:nth-child(2) > input")
    password = (By.CSS_SELECTOR, "#__next > div.content-container.signedout > div.container-fluid.h-100 > div > div.col-lg-9.d-none.d-lg-block.py-5.bg-white > div > div > div > form > div:nth-child(3) > div > input:nth-child(1)")
    signin = (By.CSS_SELECTOR, "#__next > div.content-container.signedout > div.container-fluid.h-100 > div > div.col-lg-9.d-none.d-lg-block.py-5.bg-white > div > div > div > form > div.row.py-3 > div.col-md-4.col-sm-12 > button")

    def acceptCookies(self):
        return self.driver.find_element(*SigninPage.cookies).click()

    def loginEmail(self):
        return self.driver.find_element(*SigninPage.email).send_keys("amarnadhmurapaka1997@gmail.com")

    def loginPassword(self):
        return self.driver.find_element(*SigninPage.password).send_keys("Amar@7036")

    def signin_Button(self):
        return self.driver.find_element(*SigninPage.signin).click()





