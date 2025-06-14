import random

random_number = random.randint(1,20)

while True:
        user_number = input("Enter number: ")
        if user_number.isdigit():
             user_number = int(user_number)
             if user_number <1 or user_number >20:
                print("please enter number 1 - 20")
             else:
                  if user_number == random_number:
                       print("you're the winner")
                       print("Generated number: ",random_number)
                       break
                  else:
                       print("Indixpert won")
                       print("Generated number: ",random_number)
                       break
        else:
            print("Enter only positive Numbers")    

    
        
        
        
            
                
            
                



    





