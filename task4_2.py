import keyword

def decrypt_clue(text):
    '''Finds python keywords in a text.'''
    elist = []
    file = open(text, "r")
    read = file.read()
    ListOfWords = keyword.kwlist
    count = 0
    for word in ListOfWords:
        if word in read:
            elist.append(word)

    return (elist)


TheList = decrypt_clue(r"\Users\HardLand\Desktop\pythonn\mysterious.txt")

def solve_puzzles(puzzles):
    '''Gets a value and returns its boolean form.'''

    answers = []

    file = open(puzzles, "r")
    fn = file.readlines()

    fn = list(map(lambda a: a.strip(), fn))

    for i in fn:
        if i.isdigit() == True:
            i = int(i)
            if (i == 0):
                answers.append(False)
            elif i != 0:
                answers.append(True)

        elif i.startswith("["):

            if i[:2] == "[]":
                answers.append(False)
            else:
                answers.append(True)

        elif i.startswith("{"):

            if i[:2] == "{}":
                answers.append(False)
            else:
                answers.append(True)

        elif i == "None":
            if i[:1] == "N":
             answers.append(False)
            else:
                answers.append(True)

        elif i == '""' or i == "''":
            answers.append(False)
        else:
            answers.append(True)

    return(answers)

answer = solve_puzzles(r"\Users\HardLand\Desktop\pythonn\puzzles.txt")
fanswer = [str(i) for i in answer]

start = int(input("The first number: "))
end = int(input("The second number: "))

def calculate_magic_numbers(start, end):

    '''Creates random numbers between two inputted numbers.'''

    numbers = []
    while True:
        num = float(input("Enter a number between 0 and 1: "))
        num2 = num*(end-start)+start
        numbers.append(num2)
        respond = input("Do you want to continue?")
        if respond == "No" or respond == "no":
            break

    return(numbers)

game = calculate_magic_numbers(start, end)
fgame = [str(i) for i in game]

import random
import time


def exam_numbers():

    '''It's a game of putting the decimal equivalent of a binary number.'''

    answers = []

    start = time.perf_counter()
    print("You have 20 seconds to answer.")

    while time.perf_counter() - start < 20:

        b_number = ""
        for i in range (4):
            number = random.randint(0,1)
            number = str(number)
            b_number+=number

        print(b_number)
        print("Enter the decimal form of the number")

        b_number = int(b_number)
        k = 1
        d_number=0

        while(b_number>0):
            d = b_number%10
            r = d*k
            d_number = d_number + r
            b_number = b_number//10
            k = k*2

        answer = int(input("Enter your answer:"))
        if answer == d_number:
            answers.append("correct")
        else:
            answers.append("incorrect")

    return(answers)

num_game = exam_numbers()

import string


def check_pass():
    
    '''Gets username and password, creates a tuple list for all the usernames and passwords and return a list of all the usernames with a strong password.'''

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

users = check_pass()

def unlock_vault(clue):
    FirstElement = clue[0]
    FirstChar = FirstElement[0]
    return(FirstChar)

firstone = unlock_vault(TheList)
print(firstone)
secondone = unlock_vault(fanswer)
print(secondone)
thirdone = unlock_vault(fgame)
print(thirdone)
forthone = unlock_vault(num_game)
print(forthone)
fifthone = unlock_vault(users)
print(fifthone)