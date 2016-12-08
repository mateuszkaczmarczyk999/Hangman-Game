import random
import time
import os
import sys

capitol_dict = {}

with open("countries_and_capitals.txt") as f:
    for line in f:
       (key, val) = line[:-1].split(" | ")
       capitol_dict[key.upper()] = val.upper()
f.close()

def lifes():
    """Update user's life"""
    global life
    global country

    print("You lost your life!")
    time.sleep(1)
    life -= 1
    if life < 2:
        print("Your hint: ", country)
    if life <= 0:
        os.system('clear')
        print("You LOSE!!!")
        time.sleep(1)
        play_again()

def check_letter():
    """when user want to guess letter"""
    global dashes
    global trash

    guess_letter = input("What is your letter? ")
    if not guess_letter.isalpha():
        print("Its not a letter, try again.")
        check_letter()
    guess_letter = guess_letter.upper()

    if guess_letter in letters:
        while guess_letter in letters:
            temp_list = letters
            lx = temp_list.index(guess_letter)  #guessed letter possition in word
            temp_list[lx] = " "
            dashes[lx] = guess_letter
        print(dashes)
        check_dash()
    else:
        print("Wrong letter!")
        trash.append(guess_letter)
        lifes()
        ask()

def check_dash():
    """Check if all lettres in word are guessed"""

    if "_" not in dashes:
        print("Congratulations! You are the WINNER!")
        play_again()
    else:
        ask()

def play_again():
    play_again = input("Do you wanna play again? y -yes, enything else for exit ")
    if play_again == "y":
        main()
    else:
        exit()

def check_word():
    """when user want to guess word"""

    guess_word = input("What is your word? ")
    if not guess_word.isalpha():
        print("Its not a word, try again.")
        check_word()
    guess_word = guess_word.upper()
    if guess_word == city:
        print("Congratulations! You are the WINNER!")
        play_again()
    else:
        print("Wrong word!")
        lifes()
        ask()

def ask():
    """Asking of first input and checking"""
    global trash
    global life

    time.sleep(1)
    os.system('clear')
    trash.sort()
    print("LIFE: ", life)
    print("Not-in-word letters: ", trash)
    print(dashes)
    if life <= 2:
        print("Your hint: ", country)
    else:
        print("?")
    a = input("word or letter? ")
    if a == "word":
        check_word()
    elif a == "letter":
        check_letter()
    else:
        print("Invalid command.")
        ask()

def main():
    global city
    global country

    country = random.choice(list(capitol_dict.keys()))
    city = capitol_dict[country]

    print(country)
    print(city)

    global letters
    letters = list(city)

    global dashes
    dashes = ["_"] * len(letters)

    global life
    life = 1

    global trash
    trash = []

    ask()

if __name__ == "__main__":
    main()
