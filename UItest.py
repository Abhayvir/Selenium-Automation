import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://magento.softwaretestingboard.com/")

search_display = 1
search_functional = 1
nav_functional = 1
nav_display = 1

try:
    search_bar = driver.find_element(By.ID, "search")
except:
    search_display = 0

try:
    search_bar.send_keys("Radiant Tee")
except:
    search_functional = 0

try:
    navigation_menu = driver.find_element(By.CLASS_NAME, "navigation")
except:
    nav_display = 0
try:
    nav_item = driver.find_element(By.CLASS_NAME, "level0")
    nav_item.click()
except:
    nav_functional = 0

time.sleep(10)
    
footer = driver.find_element(By.CLASS_NAME, "footer")

if search_display == 1:
    print("Search bar is displayed")
else:
    print("Search bar not displayed")
if search_functional == 1:
    print("Search bar is functional")
else:
    print("Search bar is not functional")

if nav_display == 1:
    print("Navigation menu is displayed")
else:
    print("Navigation menu is not displayed")

if nav_functional == 1:
    print("Navigation menu is functional")
else:
    print("Navigation menu is not functional")

if footer.is_displayed():
    print("Footer is displayed")

driver.quit()
