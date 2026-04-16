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
