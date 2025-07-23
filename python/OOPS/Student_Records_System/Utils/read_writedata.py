import json
from python.Programs.error_source import update_errorslog, error_details
from python.OOPS.Student_Records_System.Domain.all_paths import paths_obj
from python.Utils.file_io import file_io_obj


class DataOperations:
    def __init__(self, datapath):
        self.recordspath = datapath
        self.studentlist = file_io_obj.read_alldata(self.recordspath)

    def write_data(self):
        with open(self.recordspath, "w") as file:
            file.write(json.dumps(self.studentlist, indent=3))

file_obj = DataOperations(paths_obj.datapath)
