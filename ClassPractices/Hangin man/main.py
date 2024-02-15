import random

def hanginmanmain():
    word_list = ["lion", "rabbit", "elephant", "bird", "snake", "bull", "capibara", "ostrich", "honeybee"]
    true_word = random([word_list]) #need fixing! can't pull random!
    print("welcome to the hangin man game!")
    guess = input("guesss a letter:  ")
    answer = len(true_word) * "_"
