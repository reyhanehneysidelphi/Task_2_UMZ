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
        if respond == "No" or respond == "no" or respond == "NO":
            break

    print(numbers)

game = calculate_magic_numbers(start, end)