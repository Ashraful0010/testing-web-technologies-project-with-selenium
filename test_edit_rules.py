from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Correct driver path
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open the admin login page and login
driver.get("http://localhost/final_project/View/adminlogin.html")
time.sleep(2)

# Login as admin
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

# Step 2: Go to edit_rules.php
driver.get("http://localhost/final_project/Model/edit_rules.php")
time.sleep(2)

# Step 3: Check for Add Rule textarea and Add button
try:
    textarea = driver.find_element(By.NAME, "rules")
    print("✅ 'Add New Rule' textarea is visible.")
except:
    print("❌ 'Add New Rule' textarea not found.")

try:
    add_button = driver.find_element(By.NAME, "add_rule")
    print("✅ 'Add Rule' button found.")
except:
    print("❌ 'Add Rule' button not found.")

# Step 4: Check if existing rules table is visible
try:
    table = driver.find_element(By.TAG_NAME, "table")
    print("✅ Rules table is visible.")
except:
    print("❌ Rules table not found.")

# Step 5: Check for edit/delete buttons (if rules exist)
edit_buttons = driver.find_elements(By.NAME, "edit_rule")
delete_buttons = driver.find_elements(By.NAME, "delete_rule")

print(f"✅ Found {len(edit_buttons)} 'Edit' button(s).")
print(f"✅ Found {len(delete_buttons)} 'Delete' button(s).")
