import pandas as pd
import sys,os
sys.path.append(os.getcwd())
from python.Utils.file_io import file_io_obj
from python.web_scrap_concepts.Scrap_Html.src.Domain.scrap_paths import path_obj

class Excel:
    def __init__(self):
        pass

    def excel_read(self):
        try:
            exceldata = pd.read_excel(path_obj.npi_data_path,sheet_name=0)
            print(pd.DataFrame(exceldata))
        except Exception as err:
            print("Error logged..")
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(err),path_obj.scrap_err_log)

    def excel_write(self,links_df):
        try:
            with pd.ExcelWriter(path_obj.npi_data_path, engine="openpyxl") as excel_writer:
            # with pd.ExcelWriter(path_obj.npi_data_path, engine="openpyxl", mode="a", if_sheet_exists="new") as excel_writer:
                links_df.to_excel(excel_writer, sheet_name="Links", index=False)
        except Exception as err:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(err),path_obj.scrap_err_log)

excel_obj = Excel()
# excel_obj.excel_read()