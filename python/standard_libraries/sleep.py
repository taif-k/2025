import time


id = int(input("Enter id: "))
count = 0
while count <= 4:
    count = count + 1
    print("Searching.")
    time.sleep(0.5)
    print("Searching..")
    time.sleep(0.5)
    print("Searching...")
    

print("Entered id is ",id)