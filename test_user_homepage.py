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

# Step 1: Go to the login page
driver.get("http://localhost/final_project/View/login.html")
time.sleep(2)

# Step 2: Fill in login credentials
driver.find_element(By.NAME, "username").send_keys("opu0010")
driver.find_element(By.NAME, "password").send_keys("Abcd1234")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

# Step 3: Confirm userHome.php is reached
if "userHome.php" in driver.current_url:
    print("✅ Login successful. Now on userHome.php.")
else:
    print("❌ Login failed or wrong redirection.")
    driver.quit()
    exit()

# Step 4: Test each dashboard card
card_paths = [
    ("View Application Fees", "../Model/view_fee.php"),
    ("Open News Portal", "../Model/view_news.php"),
    ("Rulebook", "../Model/view_rules.php"),
    ("Edit Information", "../Model/user_edit.php"),
]

for index, (label, expected_href) in enumerate(card_paths):
    try:
        cards = driver.find_elements(By.CLASS_NAME, "card")
        if index < len(cards):
            print(f"✅ Clicking card: {label}")
            cards[index].click()
            time.sleep(2)

            current_url = driver.current_url
            if expected_href in current_url:
                print(f"   → Navigation success to: {expected_href}")
            else:
                print(f"   ⚠ Expected: {expected_href}, but got: {current_url}")

            driver.back()
            time.sleep(2)
        else:
            print(f"❌ Card {label} not found.")
    except Exception as e:
        print(f"❌ Error while clicking {label} card:", e)

# Step 5: Click Logout
try:
    logout_button = driver.find_element(By.CLASS_NAME, "logout-button")
    print("✅ Logout button found. Clicking...")
    logout_button.click()
    time.sleep(2)
    if "login.html" in driver.current_url:
        print("   → Successfully logged out.")
    else:
        print("⚠ Logout may not have redirected correctly.")
except Exception as e:
    print("❌ Logout failed:", e)
