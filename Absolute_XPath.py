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

# no:2


from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.instagram.com/")

driver.maximize_window()
sleep(3)

driver.find_element("xpath","(//input[contains(@class,'x1i10hfl xggy1nq xtpw4lu')])[1]").send_keys("lokesh")
sleep(3)

driver.find_element("xpath","(//input[contains(@class,'x1i10hfl xggy1nq xtpw4lu')])[2]").send_keys('loki123')
sleep(3)

driver.find_element("xpath","(//span[.='Log in'])[1]").click()
sleep(3)

driver.close()

# no:3

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.instagram.com/")

driver.maximize_window()
sleep(3)

driver.find_element("xpath","//input[@id='_r_2_']").send_keys('lokesh')
sleep(3)

driver.find_element("xpath","//input[@type='password']").send_keys('loki123')
sleep(3)

driver.find_element("xpath","(//span[.='Log in'])[1]").click()
sleep(3)

driver.close()

# no:4

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")

driver.maximize_window()
sleep(3)

driver.find_element("xpath","//a[text()='Register']").click()
sleep(3)

driver.find_element("xpath","(//a[contains(text(),'Books')])[3]").click()
sleep(3)

driver.close()

# no:5

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://www.facebook.com/")

driver.maximize_window()
sleep(3)

driver.find_element("xpath","//input[@id='_R_oiqjbjb9pb6amH1_']").send_keys("lokesh")
sleep(3)

driver.find_element("xpath","//input[@type='password']").send_keys('123445567')
sleep(3)

driver.find_element("xpath","(//span[.='Log in'])[1]").click()
sleep(3)

# no:6


from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")

driver.maximize_window()
sleep(3)

driver.find_element("xpath","//a[@href='/register']").click()
sleep(3)

driver.find_element("xpath","(//input[@type='radio'])[1]").click()
sleep(3)

driver.find_element("xpath","(//input[@type='text'])[3]").send_keys('lokesh')
sleep(3)

driver.find_element("xpath","(//input[@type='text'])[4]").send_keys("sathiyam")
sleep(3)

driver.find_element("xpath","(//input[@type='text'])[5]").send_keys("lokesh@gmail.com")
sleep(3)

driver.find_element("xpath","(//input[@type='password'])[1]").send_keys("lokesh123")
sleep(3)

driver.find_element("xpath","(//input[@type='password'])[2]").send_keys("lokesh123")
sleep(3)

driver.find_element("xpath","//input[@value='Register']").click()
sleep(3)