from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Tests_2.ProfilePage import ProfilePage
from Tests_2.conftest import driver


class LandingPage:

    def __init__(self, driver):
        self.driver = driver
    my_profile = (By.ID, "profile/me")

    def my_profilepage(self):
        return self.driver.find_element(*LandingPage.my_profile).click()




