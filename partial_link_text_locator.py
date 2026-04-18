from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.amazon.in/")
sleep(3)

driver.maximize_window()
driver.find_element("partial link text","Sell").click()
sleep(3)


# no:2

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.instagram.com/#")
driver.maximize_window()
sleep(3)

driver.find_element("partial link text","Meta").click()
sleep(3)
