import random

import time

WORDS = ("python", "jumble", "easy", "difficult", "answer", "chicken")
word = random.choice(WORDS)
correct = word
jumble = ""
livesRemaining = 3

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(
    """
          Welcome to WORD JUMBLE!!
    
          Unscramble the letters before it's to late!
          (psst..if you're too scared and you want flee press the enter key)
          """
)

time.sleep(5)

print("QUICK!! THE TITAN IS COMING! ")
print("The jumble is:", jumble)

time.sleep(2.5)
guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Ouch! That looked painful! ")
    livesRemaining -= 1
    time.sleep(2)
    print("You have " + str(livesRemaining) + " lives remaining.")
    guess = input("Your guess: ")
    if livesRemaining == 0:
        print("You're dead.")
        break
if guess == correct:
    print("YOU'RE A HERO!!! YOU DEFEATED THE UNSTOPPABLE TITAN\n")
    print("Thanks for saving the day")

input("\n\nPress the enter key to exit")

