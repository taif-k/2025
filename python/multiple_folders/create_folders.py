import check_foldername

def make_folders():
    while True:
        even_odd_name = input("1 for odd & 2 for even folder name: ")
        if even_odd_name.isdigit() and (even_odd_name == "1" or even_odd_name == "2"):
            even_odd_name = int(even_odd_name)
            if even_odd_name == 1:
                n = 1
                check_foldername.foldername(n)
                break        

            elif even_odd_name == 2:
                n = 2
                check_foldername.foldername(n)
                break

make_folders()
