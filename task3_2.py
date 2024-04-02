import random
import time


def exam_numbers():

    '''It's a game of putting the decimal equivalent of a binary number.'''
    answers = []
    
    correct_count = 0
    incorrect_count = 0

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
            correct_count = correct_count + 1
        else:
            answers.append("incorrect")
            incorrect_count = incorrect_count + 1
            
    print(answers)
    return(correct_count, incorrect_count)


print("Lets play")
game = exam_numbers()
print("The amount of correct answers, The amount of incorrect answers:")
print(game)
