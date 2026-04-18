
# css selector
#no:1

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)

driver.find_element("css selector","input[placeholder='Enter EMail']").send_keys("lokesh@gmail.com")
sleep(3)

driver.find_element("css selector","input[value=sunday]").click()
sleep(3)

driver.find_element("css selector","input[value=monday]").click()
sleep(3)

driver.find_element("css selector","input[value=tuesday]").click()
sleep(3)

driver.find_element("css selector","input[value=wednesday]").click()
sleep(3)

driver.find_element("css selector","input[value=thursday]").click()
sleep(3)

no:2

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(3)

driver.find_element("class name","ico-register").click()
sleep(3)

driver.find_element("css selector","input[value='M']").click()
sleep(3)

driver.find_element("css selector","input[class='text-box single-line']").send_keys("lokesh")
sleep(3)

driver.find_element("css selector","input[class='text-box single-line']").send_keys("sathiyam")
sleep(3)