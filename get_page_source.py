# get the source from the page source 

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)
driver=Chrome(opts)

driver.get("https://www.spacex.com/")
sleep(3)

source=driver.page_source
print("source",source)
driver.close()