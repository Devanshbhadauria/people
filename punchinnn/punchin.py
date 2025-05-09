from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = "https://ofbusiness.peoplestrong.com/altLogin.jsf"

def punch_in():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("🌐 Opening login page...")
        driver.get(LOGIN_URL)

        # Wait for username field
        print("⌛ Waiting for username field...")
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginForm:j_idt21"))
        )
        username_field.send_keys(USERNAME)
        print("✅ Username entered.")

        # Wait for password field
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginForm:j_idt25"))
        )
        password_field.send_keys(PASSWORD)
        print("✅ Password entered.")

        # Wait for login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "loginForm:j_idt29"))
        )
        login_button.click()
        print("🔐 Login button clicked.")

        # Wait for Flutter-based Punch In button — this may fail if the button is inside a canvas
        print("⌛ Waiting for Punch In button (if it's a native HTML element)...")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Punch In')]"))
        )
        punch_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Punch In')]")
        punch_btn.click()
        print("✅ Punch In clicked successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        driver.quit()
        print("🧹 Browser closed.")

if __name__ == "__main__":
    punch_in()
