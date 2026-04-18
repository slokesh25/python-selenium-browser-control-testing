from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")

driver.maximize_window()
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
sleep(3)

# sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/input").send_keys("lokesh")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/input").send_keys("sathiyam")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[4]/input").send_keys("risha@gmail.com")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[1]/input").send_keys("loki123")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[2]/input").send_keys("loki123")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[4]/input").click()
sleep(3) 

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[1]/div[1]/input").click()
sleep(3)
