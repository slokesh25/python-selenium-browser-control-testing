#closeing the browser

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)
c=Chrome(opts)  # this line is  opening the browser 
sleep(3)

c.close() # this line is close the current tab
c.quit() # closing the entire browser 
 