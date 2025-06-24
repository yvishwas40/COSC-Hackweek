from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Instagram credentials
USERNAME = "cbitcosc_demo"
PASSWORD = "Vishwas@2004"

# Path to your chromedriver
driver_path = r"C:\Users\yvish\Downloads\chromedriver\chromedriver\chromedriver.exe"
service = Service(driver_path)

# Setup Chrome options to mimic a real browser
options = Options()
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

# Step 1: Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Step 2: Wait for login fields and log in
try:
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    print("🔐 Logged in successfully.")
except:
    print("❌ Login failed. Username or password input field not found.")
    driver.quit()
    exit()

# Step 3: Handle popups (save login info, notifications)
for _ in range(2):
    try:
        not_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        not_now_button.click()
        time.sleep(2)
    except:
        break

# Step 3.5: Go to Instagram home to make sure search bar loads
driver.get("https://www.instagram.com/")
time.sleep(3)

# Step 4: Directly visit the Instagram profile
driver.get("https://www.instagram.com/cbitosc/")
time.sleep(5)
print("🔍 Navigated to @cbitosc profile.")
# Step 5: Click follow button if not already following
try:
    follow_button = wait.until(EC.presence_of_element_located((By.XPATH, "//header//button")))
    if follow_button.text.lower() == "follow":
        follow_button.click()
        print("✅ Followed @cbitosc")
    else:
        print("⚠️ Already following @cbitosc")
except Exception as e:
    print(f"❌ Follow button not found: {e}")

# Step 6: Extract profile information

try:
    full_name = wait.until(EC.presence_of_element_located((By.XPATH, "//section//span[contains(text(), 'Community')]/../../preceding-sibling::div/span"))).text
except:
    full_name = "N/A"

try:
    bio_parts = driver.find_elements(By.XPATH, "//section//div[@dir='auto' and not(ancestor::a)]")
    bio = "\n".join([b.text.strip() for b in bio_parts if b.text.strip()])
except:
    bio = "Bio not found."

try:
    stats = driver.find_elements(By.XPATH, "//ul/li//span[@class and contains(@class,'x1lliihq')]")
    posts = stats[0].text
    followers = stats[1].text
    following = stats[2].text
except:
    posts = followers = following = "N/A"

try:
    link_elem = driver.find_element(By.XPATH, "//a[contains(@href, 'linktr.ee')]")
    external_link = link_elem.get_attribute("href")
except:
    external_link = "No link found"


# Step 7: Save profile info to file
with open("cbitosc_profile.txt", "w", encoding="utf-8") as f:
    f.write(f"📸 Posts: {posts}\n")
    f.write(f"👥 Followers: {followers}\n")
    f.write(f"🔁 Following: {following}\n")
    f.write(f"🔗 Link in bio: {external_link}\n")

print("💾 Profile info saved to cbitosc_profile.txt")

# Step 8: Close browser
driver.quit()
