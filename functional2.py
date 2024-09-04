import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with your desired product name
product_name = "Radiant Tee"
email = "test@test.com"
first_name = "test"
last_name= "demo"
company = "test"
street_address = "test, demo"
city= "ohio"

zip_code = 12312
phone= 1234512345

driver = webdriver.Chrome()

driver.get("https://magento.softwaretestingboard.com/")

# Search for the product
search_box = driver.find_element(By.ID, "search")
search_box.send_keys(product_name)
search_box.send_keys(Keys.ENTER)


# Wait for product results to load
product_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, product_name))
)
product_link.click()

select_size = driver.find_element(By.ID, "option-label-size-143-item-168")
select_size.click()

select_colour = driver.find_element(By.ID, "option-label-color-93-item-57")
select_colour.click()


# Validate product in cart
# Add product to cart
add_to_cart_button = driver.find_element(By.ID, "product-addtocart-button")
add_to_cart_button.click()

time.sleep(10)

cart_link = driver.find_element(By.CLASS_NAME, "showcart")
cart_link.click()

cart_item_name = driver.find_element(By.CLASS_NAME, "product-item-name")
a_element = cart_item_name.find_element(By.TAG_NAME,"a")
a_text = a_element.text
print(a_text)

if a_text == product_name:
    print("Item validated!")
else:
    print("Try again")


checkout = driver.find_element(By.ID, "top-cart-btn-checkout")
checkout.click()

# Explicitly wait for the email field before sending keys
customer_email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

# Additional check for element visibility (optional)
if customer_email_field.is_displayed() and customer_email_field.is_enabled():
    customer_email_field.send_keys(email)
else:
    print("Error: Email field not visible or interactable")

firstname = driver.find_element(By.NAME, "firstname")
firstname.send_keys(first_name)

lastname = driver.find_element(By.NAME, "lastname")
lastname.send_keys(last_name)

company_field = driver.find_element(By.NAME, "company")
company_field.send_keys(company)

street = driver.find_element(By.NAME, "street[0]")
street.send_keys(street_address)

state = driver.find_element(By.CLASS_NAME, "select")
state.send_keys(Keys.DOWN)
state.send_keys(Keys.ENTER)

postcode = driver.find_element(By.NAME, "postcode")
postcode.send_keys(zip_code)

tele = driver.find_element(By.NAME, "telephone")
tele.send_keys(phone)

price = driver.find_element(By.NAME, "ko_unique_5")
price.click()

btn = driver.find_element(By.CLASS_NAME, "button")
btn.click()

driver.quit()