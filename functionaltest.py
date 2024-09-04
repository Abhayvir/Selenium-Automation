import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with your desired product name
product_name = "Radiant Tee"

driver = webdriver.Chrome()  # Replace with your preferred webdriver

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
# assert product_name == cart_item_name, "Product not added to cart correctly"

# Proceed to checkout (add logic for checkout steps)


driver.quit()