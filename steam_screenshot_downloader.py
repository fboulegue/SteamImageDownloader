import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# User-configurable settings
project_name = "Police"  # Project name, used for folder naming
appid = "997010"  # Steam app ID to fetch screenshots from
approx_screenshots = 24  # Approximate number of screenshots to fetch mostly more than this 

# Derived URL from appid
url = f"https://steamcommunity.com/app/{appid}/screenshots/"

# Create folder to save screenshots
save_folder = f"SteamScreenshots{project_name}"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Calculate number of scrolls needed (12 screenshots per scroll)
scroll_attempts = max(approx_screenshots // 12, 1)

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
print(f"Opening browser for {project_name} screenshots...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

time.sleep(5)  # Allow initial page load

# Perform scrolling based on calculated scroll attempts
last_height = driver.execute_script("return document.body.scrollHeight")
for i in range(scroll_attempts):
    print(f"Scrolling... ({i + 1}/{scroll_attempts})")
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("Reached the bottom of the page.")
        break
    last_height = new_height

print("Parsing page content...")
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Extract image URLs
screenshot_elements = soup.find_all("div", class_="apphub_Card")
print(f"Total screenshots found: {len(screenshot_elements)}")

for index, elem in enumerate(screenshot_elements):
    try:
        img_tag = elem.find("img")
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src'].split('?')[0]  # Remove query parameters
            print(f"Screenshot {index + 1}: {img_url}")
            img_data = requests.get(img_url).content
            img_filename = os.path.join(save_folder, f"screenshot_{index + 1}.jpg")
            with open(img_filename, "wb") as img_file:
                img_file.write(img_data)
            print(f"Downloaded: {img_filename}")
    except Exception as e:
        print(f"Failed to download screenshot {index + 1}: {e}")

print(f"Download complete for all available screenshots in folder: {save_folder}")
