from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()

driver.get("https://www.amazon.in/")
sleep(3)

driver.get("https://www.flipkart.com/")
sleep(3)

driver.back()
sleep(2)

driver.forward()
sleep(2)

driver.refresh()
sleep(2)

driver.quit()