import english_words
from english_words import english_words_alpha_set
import random
from random import choice

Wlen = 0
x = 0

# Ask User for their preferred word length(2 - 12)
while Wlen < 2 or Wlen > 12:
    x = input("How long should your word be(2 - 12 letters): ")
    if x.isdigit():
        Wlen = int(x)
# Ask the User for preferred amount of chances
Chances = 0
y = 0
while Chances < 1 or Chances > 10:
    y = input("How many chances do you want(1 - 10): ")
    if y.isdigit():
        Chances = int(y)

# Computer randomly picks a word from english_words list according to the users preference
CWlen = 0

while CWlen != Wlen:
    Cword = (random.choice(sorted(english_words_alpha_set)))
    Cword = Cword.lower()
    CWlen = len(Cword)

# Replaces letters in chosen word with *
z = 0
a = 0


Cword_list = list(Cword)
while a < CWlen:


    Cword_list[z] = "*"
    New_Word = "".join(Cword_list)
    z = z + 1
    a = a + 1
print(New_Word)

# Accepts letters from User and check if it is present in word and if it isn't decrement chances  and if it is show
# letter

b = 0
b = int(b)
req_tries = len(Cword)
used_letters = []
while Chances != 0:
    Cword_list = list(Cword)
    print(f"You Have {Chances} chances left")
    print(f"Amount of tries {req_tries}")
    print(f"Your word is {CWlen} letters long")
    print(f"Your word is {Cword}")
    print(f"Your Word is {New_Word}")
    print(f"Word list {Cword_list}")
    letter = input("Enter a letter: ")
    letter = letter.lower()

    if letter.isalpha() and len(letter) == 1 and letter in Cword_list:
        if letter in used_letters:
            print("Already used!!!!!")
            continue

        for letters in range(0, len(Cword_list)):


            if Cword_list[letters] == letter:
                    New_Word = list(New_Word)
                    New_Word[letters] = letter
                    New_Word = "".join(New_Word)
                    req_tries = req_tries - 1
                    used_letters.append(letter)




    elif letter.isalpha() == False or len(letter) != 1 or letter not in Cword_list:
        Chances = Chances - 1
        if Chances == 0:
            print("Moron!!!")
            exit()

    if req_tries == 0:
        print(f"The word is  {Cword}")
        print("Winner Winner Chicken Dinner!!!!!")
        exit()
