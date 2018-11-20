from selenium import webdriver
import time
import unittest
## TO RUNNING FROM CMD
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
## END
from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.HomePage import HomePage
import HtmlTestRunner

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/pruszlewicz/PycharmProjects/Selenium/Reports"))