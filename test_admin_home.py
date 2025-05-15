from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")  
options = Options()
options.headless = False  # Show browser for now
driver = webdriver.Chrome(service=service, options=options)

# STEP 1: Open  admin login page 
driver.get("http://localhost/final_project/View/adminlogin.html")  

# STEP 2: Fill in credentials
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")

# STEP 3: Click the Login button 
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# STEP 4: Wait to load next page
time.sleep(3)

# Step 5: Check if on adminHome.php
if "adminHome" in driver.current_url:
    print("✅ Successfully landed on adminHome.php")

    # Step 6: Verify cards by their text
    def find_card_by_text(text):
        try:
            element = driver.find_element(By.XPATH, f"//div[@class='card']//p[contains(text(), '{text}')]")
            print(f"✅ '{text}' card found")
        except:
            print(f"❌ '{text}' card NOT found")

    find_card_by_text("Edit Rules")
    find_card_by_text("Post News")
    find_card_by_text("View Users")
    find_card_by_text("Update fees")

    # Check Logout button separately 
    try:
        driver.find_element(By.LINK_TEXT, "Logout")
        print("✅ Logout link found")
    except:
        print("❌ Logout link NOT found")
else:
    print("❌ Not redirected to adminHome.php")

driver.quit()