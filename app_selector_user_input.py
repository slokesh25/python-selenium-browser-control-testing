# based on user choice of which one user wants to lunch a application

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

print("APPLICATIONS:\n1.Amazon\n2.Fliptkart\n3.Myntra")
app = int(input('Enter Your Choice '))
if app == 1:
    c=Chrome(opts)
    c.get("https://www.amazon.in/")
elif app == 2:
    c=Chrome(opts)
    c.get("https://www.flipkart.com/")
elif app == 3:
    c=Chrome(opts)
    c.get("https://www.myntra.com/")
else:
    print("Invilad Choice")