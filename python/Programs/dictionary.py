state = "delhi", "mumbai"
info = {"id":123, "fname":"taif", "state":state[0], "contact": 1234567890}

data = f""" Id is: {info["id"]}\n Name is: {info["fname"]}\n State is: {info["state"]}\n Contact is: {info["contact"]} """
print(data)


student = {}
student["id"] = 123
student["name"] = "taif"
student["contact"] = 1234567890

ispresent = "taif"

if ispresent in student.values():
    print(f"Yes {ispresent} name(value) is present in the dictionary")
else:
    print("not available")