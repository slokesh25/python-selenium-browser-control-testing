
# Based on the user input for window size

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.spacex.com/")
sleep(3)

width=int(input('Enter width'))
height=int(input('Enter height'))

driver.set_window_size(width,height)
sleep(3)
driver.close()
 