from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome driver
options = Options()
options.add_experimental_option("detach", True)
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Login first
driver.get("http://localhost/final_project/View/login.html")
time.sleep(2)

driver.find_element(By.NAME, "username").send_keys("opu0010")
driver.find_element(By.NAME, "password").send_keys("Abcd1234")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

# Step 2: Navigate to view_fee.php via direct URL or card click
driver.get("http://localhost/final_project/Model/view_fee.php")
time.sleep(2)

# Step 3: Validate table contents
try:
    table = driver.find_element(By.TAG_NAME, "table")
    headers = table.find_elements(By.TAG_NAME, "th")
    if len(headers) == 2 and headers[0].text == "Application Name" and headers[1].text == "Application Cost (tk)":
        print("✅ Table headers are correct.")
    else:
        print("❌ Table headers are incorrect or missing.")

    rows = table.find_elements(By.TAG_NAME, "tr")
    if len(rows) > 1:
        print(f"✅ Found {len(rows)-1} application fee(s) listed.")
    else:
        print("⚠ No fees found in the table.")
except Exception as e:
    print("❌ Table not found or issue in accessing fee data:", e)

# Step 4: Click 'Go Back to Homepage'
try:
    home_link = driver.find_element(By.LINK_TEXT, "Go Back to Homepage")
    print("✅ 'Go Back to Homepage' link found. Clicking...")
    home_link.click()
    time.sleep(2)
    if "userHome.php" in driver.current_url:
        print("   → Successfully returned to userHome.php.")
    else:
        print("⚠ Redirection failed or wrong destination.")
except Exception as e:
    print("❌ Error clicking homepage link:", e)
