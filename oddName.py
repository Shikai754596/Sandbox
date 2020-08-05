""" Huang Shikai """
user_name = input("Please enter your name: ")

while user_name.isspace() is True or user_name == "":
    user_name = input("Can not be blank. Please enter your name: ")

for w in user_name:
    print(w, end=" ")

