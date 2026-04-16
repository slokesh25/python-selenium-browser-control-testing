 
# lunching an application 

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

c=Chrome(opts)
c.get("https://www.amazon.in/")
sleep(3)
c.close()
