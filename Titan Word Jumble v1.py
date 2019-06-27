import random

import time


WORDS = ("python", "jumble", "easy", "difficult", "answer",  "chicken")
word = random.choice(WORDS)
correct = word
jumble = ""


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

print("QUICK!! THE TITAN IS COMING!The jumble is:", jumble)
guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Defeated by the great Titan..")
    time.sleep(2)
    print("Thanks for playing!")
    break
# elif:guess = input("Your guess: ")
if guess == correct:
    print("YOU'RE A HERO!!! YOU DEFEATED THE UNSTOPPABLE TITAN\n")
    print("Thanks for saving the day")

input("\n\nPress the enter key to exit")

















