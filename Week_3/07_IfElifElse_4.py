# Allowed users to Login

allowed_users = {"Bill": "123123", "Steve": "123456", "Peter": "1234567", "Cemil": "123654"}

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username in allowed_users:
    if password in allowed_users[username]:
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Access denied")


# Challenge
# ask for a password
# if the password doesn't match print the password is incorrect
# if the password match grant them access

