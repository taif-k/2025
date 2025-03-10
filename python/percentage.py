digit = 2
print("Digit is ",digit)

character = 't'
print("Alphabet is ",character)

english_marks = int(input("Enter english marks "))
sci_marks = int(input("enter science marks "))
math_marks = int(input("enter math marks "))
    
percentage = ((english_marks + sci_marks + math_marks)/300) * 100
print("Percentage is ",percentage)

if percentage  < 33:
    print("you failed ")

elif  percentage  >= 60:
    print("First divison ")

elif  percentage >= 50:
    print("Second division")

else:
    print("Third")

