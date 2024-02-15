import time
import random

print("hello, welcome to the hangman game!")
time.sleep(1)
print("guess the correct word")
type_list = ["animals and mythical creatures", "football players", "pc parts"]
word_list = {
    "football players": ["vinicius", "ronaldo", "messi", "benzema", "rodrygo", "haaland", "rodri", "valverde", "kane", "griezman", "casillas", "neuer"],
    "pc parts": ["rom", "ram", "hdd", "ssd", "motherboard", "cpu", "psu", "gpu", "coolant", "mouse", "keyboard", "os", "monitor", "bios", "areallycozychair"],
    "animals and mythical creatures": ["monkey", "lion", "bird", "snake", "capibara", "wolf", "parrot", "dragon", "dinosaur", "firefly", "griffin", "pegasus", "cyclops"]
} 
guesses = ""
turns = 10
category = ""
randomized = random.choice(type_list)
choice = input("""
                 select a category by choosing a number from 1-4:
                 1. animals and mythical creatures
                 2. pc parts
                 3. football players
                 4. random
                 """)
choice = int(choice)
if choice == 1:
    category = "animals and mythical creatures"
elif choice == 2:
    category = "pc parts"
elif choice == 3:
    category = "football players"
else:
    category = randomized
time.sleep(1)
print("the category is:", category)
time.sleep(1)
word = random.choice(word_list[category])

while turns != 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_ ", end="")
            failed += 1
    if failed == 0:
        print("  you won!")
        break
    guess = input("  \nguess a character:").lower()
    if len(guess) != 1:
        print("only enter a single letter")
        continue
    if guess in guesses:
        print("letter already been guessed, doesn't count as a wrong guess")
        continue
    if not guess.isalpha():
        print("only enter letters")
        continue
    guesses += guess
    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have", + turns, "more guesses")
    if turns == 0:
        print("you lose, the word was:", word)