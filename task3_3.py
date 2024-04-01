import string


def check_pass():
    usernames = []
    has_upper = False
    has_lower = False
    has_punctuation = False
    count = 0
    eTuple = []

    while True:

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        info = (username, password)
        eTuple.append(info)

        s_password = str(password)

        for counts in s_password:
            if counts.isupper() == True:
                has_upper = True
            elif counts.islower() == True:
                has_lower = True
            elif counts in string.punctuation:
                has_punctuation = True
        if len(password) > 8 and has_upper == True and has_lower == True and has_punctuation == True:
            usernames.append(username)

        respond = input("Do you want to continue?")
        if respond == "No" or respond == "no" or respond == "NO":
            break
        else:
            count = count + 1

    print(eTuple)
    return (usernames)


print("Usernames ")
users = check_pass()
print(users)