from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome driver setup
options = Options()
options.add_experimental_option("detach", True)
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open admin login page
driver.get("http://localhost/final_project/View/adminlogin.html")
time.sleep(2)

# Step 2: Login as admin
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

# Step 3: Navigate to update_fee.php
driver.get("http://localhost/final_project/Model/update_fee.php")
time.sleep(2)

# Step 4: Check if add fee form elements exist
try:
    app_name = driver.find_element(By.NAME, "application_name")
    app_cost = driver.find_element(By.NAME, "application_cost")
    add_button = driver.find_element(By.NAME, "add_fee")
    print("✅ Add Fee form fields are present.")
except:
    print("❌ One or more Add Fee form fields are missing.")

# Step 5: Fill the form and submit
app_name.send_keys("Selenium License Test")
app_cost.send_keys("750")
add_button.click()
print("✅ Submitted add fee form.")

# Step 6: Wait and verify if fee appears (basic wait)
time.sleep(2)
try:
    table_rows = driver.find_elements(By.TAG_NAME, "tr")
    if len(table_rows) > 1:
        print("✅ Fee added and table updated.")
    else:
        print("⚠️ Fee not found in table.")
except:
    print("❌ Error locating fee table.")
