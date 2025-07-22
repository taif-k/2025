from python.student_qualification.src.Domain.register_students import student_obj
from python.student_qualification.src.Domain.paths import diff_path_obj
from python.Programs.error_source import error_details,update_errorslog

class Search:
    def __init__(self):
        pass
    
    def student_search(self):
        try:
            while True:
                qualification_search = input("Enter qualification to search: ")

                if qualification_search.isalnum():
                    ispresent = False

                    for single_student_dict in student_obj.studentlist:
                        for each_qualification_dict in single_student_dict["qualification"]:
                            if qualification_search.lower() == each_qualification_dict["qname"].lower():
                                print(
                                    f"Student Name: {single_student_dict["name"]}")
                                ispresent = True
                    if ispresent == False:
                        print("qualification not found")
                    break
                else:
                    print("Enter valid qualification: ")
        except Exception as e:
            update_errorslog(error_details(e),diff_path_obj.errorlog_path)

search_obj = Search()
