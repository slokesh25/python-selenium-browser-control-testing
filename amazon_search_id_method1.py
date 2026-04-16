# method 1 for id selector 

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)

search_tf=driver.find_element("id","twotabsearchtextbox")
search_tf.send_keys("mobiles")
sleep(3)

search_btn=driver.find_element("id","nav-search-submit-button")
search_btn.click()
