  
# get the current utl of the webpage 

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.spacex.com/")
sleep(3)

url=driver.current_url
print("url:",url)
driver.close()