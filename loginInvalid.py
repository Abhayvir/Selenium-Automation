import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


username_valid = "student"
password_valid = "Password123"

username_invalid = "invalid_user"
password_invalid = "wrong_password"

driver = webdriver.Chrome()


driver.get("https://practicetestautomation.com/practice-test-login/")


# invalid username
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username_invalid)
password_field.send_keys(password_valid)

time.sleep(3)

login_button = driver.find_element(By.ID, "submit")
login_button.click()


error_message = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "error"))
)


if "Your username is invalid!" in error_message.text:
    print("Invalid Login Test (Username) Passed - Error message displayed!")
else:
    print("Invalid Login Test (Username) Failed - Unexpected error message!")


# invalid password

username_field.clear()
username_field.send_keys(username_valid)
password_field.clear()
password_field.send_keys(password_invalid)

time.sleep(3)
login_button.click()


error_message = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "error"))
)
time.sleep(3)

if "Your password is invalid!" in error_message.text:
    print("Invalid Login Test (Password) Passed - Error message displayed!")
else:
    print("Invalid Login Test (Password) Failed - Unexpected error message!")


driver.quit()