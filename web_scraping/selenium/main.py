#!/home/douglasmg7/miniconda3/envs/web_scraping/bin/python3
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

website = "https://www.adamchoi.co.uk/overs/detailed"
chromedriver_path = "/usr/bin/chromedriver"

options = Options()
# options.binary_location = "/usr/bin/chromedriver"
options.binary_location = "/usr/bin/chromium"
# options.add_experimental_option("detach", True)

# Optional optimization arguments
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome(chromedriver_path)
driver.get(website)
# //label[text()='Over 3.5']
# //label[text()='All matches']
btn = driver.find_element(By.XPATH, "//label[text()='All matches']")
btn.click()
print(f"btn: {btn}")
time.sleep(3)
driver.quit()
