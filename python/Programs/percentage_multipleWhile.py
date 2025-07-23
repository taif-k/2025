from python.Utils.file_io import file_io_obj
import json
import sys
import os
sys.path.append(os.getcwd())


def highest_percentage():
    try:
        listdata = []
        percentagelist = []

        for num in range(1, 3):
            studentdata = {}
            markslist = []
            marksdict = {}
            count = 0

            studentdata["id"] = int(input("Enter id: "))
            studentdata["name"] = input("Enter name: ")
            studentdata["marks"] = markslist
            while count == 0:
                marks = int(input("Enter Hindi marks (0 - 100): "))
                if marks >= 0 and marks <= 100:
                    marksdict["hindi"] = marks
                    while count == 0:
                        marks = int(input("Enter English marks (0 - 100): "))
                        if marks >= 0 and marks <= 100:
                            marksdict["english"] = marks
                            while count == 0:
                                marks = int(
                                    input("Enter Math marks (0 - 100): "))
                                if marks >= 0 and marks <= 100:
                                    marksdict["math"] = marks
                                    while count == 0:
                                        marks = int(
                                            input("Enter Science marks (0 - 100): "))
                                        if marks >= 0 and marks <= 100:
                                            marksdict["science"] = marks
                                            count = 1
            markslist.append(marksdict)
            listdata.append(studentdata)
            percentagelist.append(
                (marksdict["hindi"] + marksdict["english"] + marksdict["math"] + marksdict["science"])/400 * 100)

        print(markslist)
        print(json.dumps(listdata, indent=3))
        percentagelist.sort()
        print(percentagelist)
        print("Highest percentage is: ", percentagelist[-1])
    except Exception as e:
        print("Enter valid data...Checking error log to resolve error")
        file_io_obj.update_errorslog(
            file_io_obj.get_errdetails(e), file_io_obj.error_path)


highest_percentage()
