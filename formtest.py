import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

full_name = "test"
email = "test@demo.com"
phone= 1234512345
other= "test demo"

driver = webdriver.Chrome()

driver.get("https://qavalidation.com/demo-form/#google_vignette")


fullname = driver.find_element(By.NAME, "g4072-fullname")
fullname.send_keys(full_name)

email = driver.find_element(By.NAME, "g4072-email")
email.send_keys(email)

tele = driver.find_element(By.NAME, "g4072-phonenumber")
tele.send_keys(phone)

gender = driver.find_element(By.CLASS_NAME, "g4072-yearsofexperience-2")
gender.send_keys(Keys.DOWN)
gender.send_keys(Keys.ENTER)

# gender = driver.find_element(By.CLASS_NAME, "g4072-yearsofexperience-2")
# state.send_keys(Keys.DOWN)
# state.send_keys(Keys.ENTER)



btn = driver.find_element(By.CLASS_NAME, "button")
btn.click()

driver.quit()