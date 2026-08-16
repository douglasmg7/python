#!/home/douglasmg7/miniconda3/envs/web_scraping/bin/python3
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
# print(f"btn: {btn}")
btn.click()

dropdown_season = driver.find_element(By.XPATH, "//select[@id='season']")
dropdown = Select(dropdown_season)

# Print text and value for every option in the dropdown
# for option in dropdown.options:
#     print(f"Text: {option.text} | Value: {option.get_attribute('value')}")

# drop_down.select_by_value("object:203")
# dropdown.select_by_index(1)
dropdown.select_by_visible_text("2025/2026")

time.sleep(2)
# matches = driver.find_elements(By.XPATH, "//tr")
matches = driver.find_elements(By.TAG_NAME, "tr")
# print(matches)

date = []
home_team = []
score = []
away_team = []

print("matches count:", len(matches))
for match in matches:
    # print(match.text)
    tds = match.find_elements(By.XPATH, "./td")
    if len(tds) > 1:
        # print(f"tds len: {len(tds)}")
        # print("0", tds[0].text)
        date.append(tds[0].text)
        # print("2", tds[2].text)
        home_team.append(tds[2].text)
        # print("3", tds[3].text)
        score.append(tds[3].text)
        # print("4", tds[4].text)
        away_team.append(tds[4].text)

for i in range(20):
    print(f"{date[i]} - {home_team[i]} - {score[i]} - {away_team[i]}")

time.sleep(3)
driver.quit()
