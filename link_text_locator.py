# find the text locator
# no:1

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.instagram.com/#")
sleep(3)

driver.find_element("link text","Meta").click()
sleep(3)
driver.close()

# no:2

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.saucedemo.com/")
sleep(3)

driver.find_element("id","user-name").send_keys("lokesh")
sleep(3)

driver.find_element("id","password").send_keys("loki123")
sleep(3)

driver.find_element("link text","Login").click()
sleep(3)

# no:3

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts=ChromeOptions()
opts.add_experimental_option("detach",True)
driver=Chrome(opts)
driver.get("https://www.instagram.com/#")
sleep(3)
driver.find_element("link text","Forgot password?").click()
sleep(3)
driver.close()