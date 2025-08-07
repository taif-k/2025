import sys,os
sys.path.append(os.getcwd())
from python.Utils.file_io import file_io_obj

def main():
    try:
        print("Student 1")
        student1 = {"studentid":101}
        student1["hindi"] = int(input("Enter Hindi Marks"))
        student1["english"] = int(input("Enter English Marks"))
        student1["math"] = int(input("Enter Math Marks"))
        student1["science"] = int(input("Enter Science Marks"))

        percentage1 = (student1["hindi"] + student1["english"] + student1["math"] + student1["science"])/400 * 100
        print("Percentage for student 1: ",percentage1)
        if percentage1 >= 60:
            print("First division")
        else:
            if percentage1 >=45:
                print("Second Division")
            elif percentage1 >=33:
                print("Third Division")
            else:
                print("Failed")

        print("\nStudent 2")
        student2 = {"studentid":102}
        student2["hindi"] = int(input("Enter Hindi Marks"))
        student2["english"] = int(input("Enter English Marks"))
        student2["math"] = int(input("Enter Math Marks"))
        student2["science"] = int(input("Enter Science Marks"))
        
        percentage2 = (student2["hindi"] + student2["english"] + student2["math"] + student2["science"])/400 * 100
        print("Percentage for student 2: ",percentage2) 
        
        if percentage2 >= 60:
            print("First division")
        else:
            if percentage2 >=45:
                print("Second Division")
            elif percentage2 >=33:
                print("Third Division")
            else:
                print("Failed")    
                
        if percentage1 > percentage2:
            print("\nStudent 1 is Topper")
        else:
            print("\nStudent 2 is topper")
    except Exception as e:
        print("Marks should be in digits only")
        file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),file_io_obj.error_path)

        main()

main()