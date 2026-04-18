# method 1 for id selector --> (2 methods only)

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


 # method 2 for id selector
 
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)

driver.find_element("id","twotabsearchtextbox").send_keys("mobiles")
sleep(2)

driver.find_element("id","nav-search-submit-button").click()


# this is not method id locator scripts
# no:1

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.instagram.com/?hl=en")
sleep(3)

# insta id can change when we refresh a page so it's giveing error for sometimes 
driver.find_element("id","_R_c9d9lplkldcpbn6b5ipamH1_").send_keys("lokesh")
sleep(3)

driver.find_element("id","_R_cdd9lplkldcpbn6b5ipamH1_").send_keys("loki234")
sleep(3)

driver.close()

# no:2
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.saucedemo.com/")
sleep(3)

driver.find_element("id","user-name").send_keys("lokesh")
sleep(3)

driver.find_element("id","password").send_keys("loki123")
sleep(3)

# This line login button is not click because login name is attribute
# it's not center of the tag <input>login</input> like this so it's not execute
driver.find_element("link text","Login").click()
sleep(3)