from selenium.webdriver.common.by import By
from POMDemo.Locators.HomePageLocators import HomePageLocators

class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):

        self.driver.find_element(By.ID, HomePageLocators.welcome_link).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, HomePageLocators.logout_link).click()