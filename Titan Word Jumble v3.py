import random

import time

from threading import Timer

livesRemaining = 3  # Including a life system
WORDS = ["python", "jumble", "easy", "difficult", "answer", "chicken"]
level_number = 1
print(
    """
          Welcome to WORD JUMBLE!!

          Unscramble the letters before it's to late!
          
          YOU HAVE 3 LIVES!
          """
)

time.sleep(3)
# print("The jumble is:", jumble)

# guess = input("Your guess: ")
# guess = input("Your guess: ")
def create_jumble(word):
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    return jumble;

while len(WORDS) > 0:
    currentWords = WORDS[0]
    print("QUICK!! THE TITAN IS COMING!")
    print("The jumble is:", create_jumble(currentWords))
    guess = input("Your guess: ")

    if guess == currentWords:
        print("Well done you passed this level!")
        WORDS.remove(currentWords)

    else:
        if livesRemaining > 1:
            livesRemaining -= 1
            print("You have " + str(livesRemaining) + " lives remaining.")
        else:
            print("Game over sucker!")
            break


input("\n\nPress the enter key to exit the game")





# def timeout():
#     print("Game over")
# t = Timer(5, timeout)
# t.start()
#
# t.join()

#level variable
