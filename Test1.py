from selenium import webdriver
import time

driver = webdriver.Chrome("drivers\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("automation step by step")
time.sleep(1)
driver.find_element_by_name("btnK").click()

time.sleep(2)

driver.close()
driver.quit()

print("Test completed")