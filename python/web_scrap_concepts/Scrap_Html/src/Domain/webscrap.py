import sys
import os
sys.path.append(os.getcwd())
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup
from python.web_scrap_concepts.Scrap_Html.src.Domain.op_on_excel import Excel
from python.web_scrap_concepts.Scrap_Html.src.Domain.scrap_paths import path_obj
from python.Utils.file_io import file_io_obj

class Scrap:
    def __init__(self):
        self.excel_writer = Excel()
        self.link_data = self.excel_writer.excel_read()
        
    def scrap_content(self):
        try:
            browser_handler = webdriver.Chrome(service=Service(ChromeDriverManager().install())) ##
        
            browser_handler.get("https://npiregistry.cms.hhs.gov/search")
            time.sleep(5)

            rendered_html = browser_handler.page_source
            # print(type(rendered_html))
            parsed_html = BeautifulSoup(rendered_html, "lxml") 
            # print(type(parsed_html))

                        
            self.link_data = [] 
            for a_tag in parsed_html.find_all("a"):
                link_text = a_tag.text.strip()
                href = a_tag.get("href")
                self.link_data.append({"link_text": link_text,"url": href})  
                                      
            self.df_links = pd.DataFrame(self.link_data)
            self.excel_writer.excel_write(self.df_links)

            # logging program run datetime
            file_io_obj.update_errorslog(data=file_io_obj.get_errdetails(get_date=True), path=path_obj.program_run_capture)
            browser_handler.quit()

        except Exception as err:
            print("error logged")
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(err), path_obj.scrap_err_log)


scrap_obj = Scrap()
