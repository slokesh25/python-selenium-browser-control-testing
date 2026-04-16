 # method 2 for id selector

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)

driver.find_element("id","twotabsearchtextbox").send_keys("mobiles")
sleep(2)

driver.find_element("id","nav-search-submit-button").click()