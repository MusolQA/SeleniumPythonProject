from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = "drivers/geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleep(1)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title)
driver.close()
