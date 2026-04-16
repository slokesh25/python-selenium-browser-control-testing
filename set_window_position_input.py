# Based on the user input for window position size 

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.spacex.com/")
sleep(3)

Xaxis=int(input('Enter Xaxis'))
Yaxis=int(input('Enter Yaxis'))

driver.set_window_position(Xaxis,Yaxis)
sleep(3)
driver.close()