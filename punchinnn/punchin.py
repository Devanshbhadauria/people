from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = "https://ofbusiness.peoplestrong.com/altLogin.jsf"  # Replace with actual login URL

def punch_in():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    # For debugging, remove headless mode
    # options.add_argument('--headless')  # Uncomment to run headless in production

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("Opening login page...")
        driver.get(LOGIN_URL)

        # Wait for username input field to be present
        print("Waiting for username field...")
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        print("Username field located.")
        
        username_field.send_keys(USERNAME)
        print("Entering password...")

        # Wait for password input field to be present
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(PASSWORD)

        # Wait for login button to be clickable
        print("Waiting for login button to be clickable...")
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "loginButton"))
        )
        print("Clicking login button...")
        login_button.click()

        # Wait for page to load after login
        print("Waiting for Punch In button...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Punch In')]"))
        )

        # Now click the "Punch In" button
        print("Clicking Punch In button...")
        punch_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Punch In')]")
        punch_btn.click()

        print("✅ Punch In successful")

        # Debugging: Save the page source in case you want to inspect it
        with open("punchin_page_source.html", "w") as f:
            f.write(driver.page_source)

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    punch_in()
