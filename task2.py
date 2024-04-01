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

    return (answers)


print("Let's find the answer:")

answer = solve_puzzles(r"\Users\HardLand\Desktop\pythonn\puzzles.txt")
print(answer)