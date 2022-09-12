import time
from lib2to3.pgen2 import driver
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from Tests_2.SigninPage import SigninPage
from Utilities_2.BaseClass import BaseClass
from Tests_2.LandingPage import LandingPage


class TestReskill(BaseClass):

    def test_signin(self):

        signinpage = SigninPage(self.driver)
        log = self.getLogger()
        signinpage.acceptCookies()
        log.info("Accepting Cookies")
        signinpage.loginEmail()
        log.info("Entering Email")
        signinpage.loginPassword()
        log.info("Entering Password")
        signinpage.loginButton()
        #landingpage = LandingPage(self.driver)
        #landingpage.referButton()
        time.sleep(25)















