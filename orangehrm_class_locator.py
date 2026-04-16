
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(3)

driver.find_element("class name","oxd-input.oxd-input--active").send_keys("loki2545")
sleep(3)

driver.find_element("class name","oxd-input.oxd-input--active").send_keys("lokesh")
sleep(3)

driver.close()