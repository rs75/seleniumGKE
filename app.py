from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path

chrome_options = Options()
chrome_options.add_argument("--headless")

fpath = Path("chromedriver").absolute()
driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver")

driver.get("https://google.com")

with open("temp.txt", "w") as f:
    f.write(driver.page_source)


