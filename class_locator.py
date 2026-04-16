from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)

driver.find_element("class name","form-control").send_keys("lokesh")
sleep(3)

driver.find_element("class name","form-control").send_keys("lokesh@gmail")