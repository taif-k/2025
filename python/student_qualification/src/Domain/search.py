from python.student_qualification.src.Domain.paths import diff_path_obj
from python.Utils.file_io import file_io_obj

class Search:
    def __init__(self):
        self.studentlist = file_io_obj.read_alldata(diff_path_obj.records_path)
    
    def student_search(self):
        try:
            while True:
                qualification_search = input("Enter qualification to search: ")

                if qualification_search.isalnum():
                    ispresent = False

                    for single_student_dict in self.studentlist:
                        for each_qualification_dict in single_student_dict["qualification"]:
                            if qualification_search.lower() == each_qualification_dict["qname"].lower():
                                print(f"\n\nStudent with searched Qualification: {single_student_dict["name"]}\n")
                                ispresent = True
                    if ispresent == False:
                        print("qualification not found")
                    break
                else:
                    print("Enter valid qualification: ")
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),diff_path_obj.errorlog_path)

search_obj = Search()
