from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username_valid = "student"
password_valid = "Password123"

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username_valid)
password_field.send_keys(password_valid)

login_button = driver.find_element(By.ID, "submit")
login_button.click()

WebDriverWait(driver, 5).until(EC.url_contains("https://practicetestautomation.com/logged-in-successfully/"))

if driver.current_url == "https://practicetestautomation.com/logged-in-successfully/":
    print("Valid Login Test Passed - Logged in successfully!")
    logout_button = driver.find_element(By.CLASS_NAME, "wp-block-button__link")
    logout_button.click()
else:
    print("Valid Login Test Failed - Unexpected title!")

driver.quit()