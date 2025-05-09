# ADD THIS at the top
from bs4 import BeautifulSoup

# REPLACE the try block with this:
try:
    print("🌐 Opening login page...")
    driver.get(LOGIN_URL)

    # Wait for JS to load the page
    time.sleep(10)

    # Dump HTML content for debug
    page_source = driver.page_source
    with open("page_dump.html", "w", encoding="utf-8") as f:
        f.write(page_source)
    print("📄 Saved page HTML to page_dump.html")

    # Use BeautifulSoup to verify elements
    soup = BeautifulSoup(page_source, "html.parser")
    if soup.find(id="loginForm:j_idt21") is None:
        print("❌ Could not find username field in HTML.")
    else:
        print("✅ Found username field in HTML.")

    # Try locating username field with Selenium
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginForm:j_idt21"))
    )
    username_field.send_keys(USERNAME)
    print("✅ Username entered.")

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginForm:j_idt25"))
    )
    password_field.send_keys(PASSWORD)
    print("✅ Password entered.")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "loginForm:j_idt29"))
    )
    login_button.click()
    print("🔐 Login button clicked.")

except Exception as e:
    print(f"❌ Error: {e}")
    # Save page source in case of error
    with open("error_page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
finally:
    driver.quit()
    print("🧹 Browser closed.")
