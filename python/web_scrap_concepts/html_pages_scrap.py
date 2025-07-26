from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time,json
import pandas as pd
from selenium.webdriver.chrome.options import Options # remove if using ChromeDriverManager

home_url = "https://www.academy.indixpert.com/"

# new ver of selenium and py cant detect CHROME loc, so manually setting up. (to avoid manuall driver setup and chrome loc , use ChromeDriverManager)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # just use inplace of ln 18 
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
options.add_argument("--start-maximized")  # opens browser in full screen

# manually appending path of chrome driver for faster run instead of using ChromeDriverManager.install() (which returns path of driver exe)
driver = webdriver.Chrome(service=Service(r"C:\Users\DELL\.wdm\drivers\chromedriver\win64\138.0.7204.169\chromedriver-win64\chromedriver.exe"), options=options)
driver.get(home_url)
time.sleep(5)
home_rendered_html = driver.page_source 
home_parsed_html = BeautifulSoup(home_rendered_html, "lxml")


footer_links = {}
for a in home_parsed_html.find_all("a"):
    text = a.text.strip()
    href = a.get("href")
    if text in ["Product Studio", "Technology Hub"] and href:
        footer_links[text] = href

all_data = []
for name, url in footer_links.items():
    driver.get(url)
    time.sleep(5)
    footer_rendered_html = driver.page_source
    footer_parsed_html = BeautifulSoup(footer_rendered_html, "lxml")

    h2_data = []
    for h2 in footer_parsed_html.find_all("h2"):
        h2_data.append({"page": name, "h2_text": h2.get_text(strip=True)})
    all_data.extend(h2_data)

print("final h2_data[]")
print(json.dumps(h2_data,indent=3))  
print("final all_data[]") 
print(json.dumps(all_data,indent=4))

df = pd.DataFrame(all_data)
print(pd)
driver.quit()

