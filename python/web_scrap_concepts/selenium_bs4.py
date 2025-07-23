from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 

driver.get("https://npiregistry.cms.hhs.gov/search")
time.sleep(2)  

html = driver.page_source 
soup = BeautifulSoup(html, "html.parser")

title = soup.title.string
print("Page Title:", title)

print("\n"" All H2 ")
for h2 in soup.find_all("h2"): 
    print(h2.get_text(strip=True))


print()

print()
for a in soup.find_all("a"):
    print("Link text:", a.text.strip())
    print("URL:", a.get("href"))

driver.quit()  ##



