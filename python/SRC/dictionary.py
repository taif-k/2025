state = "delhi", "mumbai"
info = {"id":123, "fname":"taif", "state":state[0], "contact": 1234567890}

data = f""" Id is: {info["id"]}\n Name is: {info["fname"]}\n State is: {info["state"]}\n Contact is: {info["contact"]} """
print(data)
print("\n",state)