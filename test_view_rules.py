from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Login First
driver.get("http://localhost/final_project/View/login.html")
driver.find_element(By.NAME, "username").send_keys("opu0010")
driver.find_element(By.NAME, "password").send_keys("Abcd1234")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

# Navigate to Rulebook
driver.get("http://localhost/final_project/Model/view_rules.php")
time.sleep(2)

# Check that rules table has at least one row
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
if rows:
    print("✅ Rules are displayed.")
else:
    print("❌ No rules found!")

driver.quit()
