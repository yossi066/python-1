student = {
    "name":"Mark",
    "student_id": 15163,
    "feedback":None
}

student["last_name"] = "Kawalski"
try:
    last_name = student ["last_name"]
    numbered_last_name = 3 + last_name

except KeyError:
    print("Error finding last_name")

except TypeError:
    print("I cant add these two together!")


print("This code executes!")
