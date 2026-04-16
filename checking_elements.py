from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.python.org/")
sleep(3)

a=driver.find_elements("tag name","div")
print(a)
print(len(a))
driver.close()