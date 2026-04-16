#opening the browser

from selenium.webdriver import Chrome,ChromeOptions
opts=ChromeOptions()
opts.add_experimental_option("detach",True)
c=Chrome(opts)
  