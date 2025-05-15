from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Setup Chrome WebDriver
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Go to login page
    driver.get("http://localhost/final_project/View/login.html")
    time.sleep(1)

    # Step 2: Fill in login credentials
    driver.find_element(By.NAME, "username").send_keys("opu0010")
    driver.find_element(By.NAME, "password").send_keys("Abcd1234")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)

    # Step 3: Go to view_news.php
    driver.get("http://localhost/final_project/Model/view_news.php")
    time.sleep(2)

    # Step 4: Check for news items
    news_items = driver.find_elements(By.CLASS_NAME, "news-item")

    if news_items:
        print(f"✅ {len(news_items)} news item(s) displayed.")
    else:
        # If no .news-item elements, check if "No news available" message is shown
        message = driver.find_element(By.TAG_NAME, "body").text
        if "No news available to display." in message:
            print("ℹ️ No news available to display.")
        else:
            print("❌ Could not determine news status.")

finally:
    # Close the browser
    driver.quit()
