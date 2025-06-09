import random
while True:
    magicNum = random.randint(1,100)

    print("I'm thinking of a number from 1 to 100, guess what number?")

    userNum = 0

    while userNum != magicNum:

        userNum = int(input("guess!\n"))

        if userNum == magicNum:
            print("You guessed right, not bad!")
            break
        elif userNum < magicNum:
            print("Wrong, my number is higher.")
            continue
        elif userNum > magicNum:
            print('Wrong, my number is lower')

    if input("do you want to play again? (y/n)") != 'y':
        break