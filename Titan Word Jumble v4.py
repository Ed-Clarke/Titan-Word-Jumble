import random

import time

livesRemaining = 3

LEVEL_1 = ["cake", "beam", "leaf", "wave"]
LEVEL_2 = ["chicken", "fishing", "python"]

LEVELS = [LEVEL_1, LEVEL_2]

print(
    """
          Welcome to WORD JUMBLE!!

          Unscramble the letters before the TITANS catch you!

          YOU HAVE 3 LIVES - GOOD LUCK!
          """
)

time.sleep(3)


def create_jumble(word):
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    return jumble


while len(LEVELS) > 0:
    currentLevel = LEVELS[0]

    while len(currentLevel) > 0:
        currentWords = currentLevel[0]
        print("QUICK!! THE TITAN IS CATCHING UP!")
        time.sleep(1.5)
        print("The jumble is:", create_jumble(currentWords))
        guess = input("Your guess: ")

        if guess == currentWords:
            time.sleep(1)
            print("Well done you've got this word correct!")
            currentLevel.remove(currentWords)

        else:
            livesRemaining -= 1
            if livesRemaining > 0:
                print("You have " + str(livesRemaining) + " lives remaining.")
            else:
                print("Game over sucker!")
                break

    if livesRemaining > 0:
        LEVELS.remove(currentLevel)
        time.sleep(2)
        print("")
        print("WELL DONE FOR COMPLETING THE LEVEL")
    else:
        break

input("\n\nPress the enter key to exit the game")

# def timeout():
#     print("Game over")
# t = Timer(5, timeout)
# t.start()
#
# t.join()

# level variable
