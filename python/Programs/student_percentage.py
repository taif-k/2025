student1 = {"studentid":101,"hindi":70,"English":60,"Math":65,"science":75}
student2 = {"studentid":102,"hindi":25,"English":23,"Math":15,"science":24}
percentage1 = (student1["hindi"] + student1["English"] + student1["Math"] + student1["science"])/400 * 100
print("Percentage for student 1: ",percentage1) 

if percentage1 >= 60:
    print("First division")
elif percentage1 <60 and percentage1 >=33:
    print("Second division")
else:
    print("Third divion") 


percentage2 = (student2["hindi"] + student2["English"] + student2["Math"] + student2["science"])/400 * 100
print("Percentage for student 2: ",percentage2) 

if percentage2 >= 60:
    print("First division")
elif percentage2 <60 and percentage2 >=33:
    print("Second division")
else:
    print("Third divion")     

if percentage1 > percentage2:
    print("\nStudent 1 is Topper")
else:
    print("\nStudent 2 is topper")
