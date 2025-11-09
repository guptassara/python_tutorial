username = str(input("Enter your user name: "))
if not username.isalpha():
    print("Your username has digits")
elif username.count(" ") > 0:
    print("Your username has spaces")
elif len(username) > 15:
    print("Your username has more than 15 characters")
else:
    print(f"You are accepted {username}")
