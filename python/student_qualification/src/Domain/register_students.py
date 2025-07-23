from python.Utils.file_io import file_io_obj
from python.student_qualification.src.Domain.paths import diff_path_obj

class Registration:
    def __init__(self):
        self.studentlist = file_io_obj.read_alldata(diff_path_obj.records_path)

    def student_registration(self):
        try:
            for num in range(1, 4):
                studentdata = {}
                qualificationlist = []
                studentdata["id"] = num
                studentdata["name"] = input("Enter name: ")
                studentdata["joined_date"] = file_io_obj.get_errdetails(get_date=True)
                studentdata["qualification"] = qualificationlist

                while True:
                    qualificationdict = {}
                    qualificationdict["qname"] = input("Enter qualification: ")
                    qualificationdict["passingyear"] = input("Enter passing year")
                    qualificationlist.append(qualificationdict)

                    ask_qualification = input("Add More qualification - y or n: ")

                    if ask_qualification.lower() != "y":
                        break

                self.studentlist.append(studentdata)
                file_io_obj.write_data(self.studentlist,diff_path_obj.records_path)
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),diff_path_obj.errorlog_path)

student_obj = Registration()
