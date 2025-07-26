from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # use this to avoid manuall detect chrome browser(.option()) and setuo driver path
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


class ScrapPages:

    def __init__(self):
        self.browser_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # extracting footer links from home page
    def get_footer_links(self):
        self.browser_driver.get("https://www.academy.indixpert.com/")
        time.sleep(4)

        home_rendered_html = self.browser_driver.page_source
        home_parsed_html = BeautifulSoup(home_rendered_html, "lxml")

        footer_links = {}
        for a in home_parsed_html.find_all("a"):
            text = a.text.strip()
            href = a.get("href")
            if text in ["Product Studio", "Technology Hub"] and href:
                footer_links[text] = href

        return footer_links
    
    # scrap footer links 
    def scrap_data(self,page_name, page_url):
        self.browser_driver.get(page_url)
        time.sleep(4)
        rendered_html = self.browser_driver.page_source
        parsed_html = BeautifulSoup(rendered_html, "lxml")

        h2_data = []
        for h2 in parsed_html.find_all("h2"):
            h2_data.append({"page": page_name, "h2_text": h2.get_text(strip=True)})

        return h2_data
    
    # save df to excel
    def write_excel(self,df):
        with pd.ExcelWriter(r"D:\Repositories\2025\python\web_scrap_concepts\test_ocr_api_scrap\scrap_multiple_html\excel.xlsx") as writer:
            df.to_excel(writer, sheet_name="Sheet1")  
        print(df)
        
    def main(self):
        links = self.get_footer_links()

        all_data = []
        for name, url in links.items():
            data = self.scrap_data(name, url)
            all_data.extend(data)
        
        df = pd.DataFrame(all_data)
        self.write_excel(df)
        
        self.browser_driver.quit()


scrap_obj = ScrapPages()
scrap_obj.main()
