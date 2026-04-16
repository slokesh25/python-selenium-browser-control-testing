
# get the title of the webpage 

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.spacex.com/")
# driver.get("https://www.amazon.in/")
sleep(3)

driver.maximize_window()
title=driver.title

print("title:",title)
driver.close()