import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome_options = webdriver.ChromeOptions()
#chrome_options = Options()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome("drivers\\chromedriver.exe")

driver.get("http://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleep(2)
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()
print("Complete")
