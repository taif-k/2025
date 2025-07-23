from python.OOPS.Student_Records_System.Domain.all_paths import paths_obj
from python.Utils.file_io import file_io_obj


class DataOperations:
    def __init__(self, datapath):
        try:
            self.recordspath = datapath
            self.studentlist = file_io_obj.read_alldata(self.recordspath)
        except Exception as e:
            print("Error logged...Try again after some time")
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e))

file_obj = DataOperations(paths_obj.datapath)
