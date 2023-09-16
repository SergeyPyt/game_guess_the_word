from random import choice, sample
from pathlib import Path
from func import func

from PIL import Image

from constants import LETTERS


def get_guess_word(word_list):
    word = choice(word_list)
    return word


def get_photos(picture_dictionary, word):
    rand_list = []
    for w in picture_dictionary:
        if word in picture_dictionary[w]:
            rand_list.append(w)

    rand_elements = sample(rand_list, 2)
    for elements in rand_elements:
        img = Image.open(Path('static', elements))
        new_size = (240, 320)
        img.thumbnail(new_size)
        img.show()
        img.close()


def guess(word):
    res = ['*'] * len(word)
    count = 0
    print(f'''Welcome to guess the word game.\n
    I made a word "{"".join(res)}" of {len(word)} letters, you have to guess it.''')

    while True:

        if "".join(res) == word:
            print('Welcome to guess the word')
            break

        char = input('Enter a letter or whole word: ').lower()

        if func(char, word) == word:
            return print(f"You guessed the word right away. You guessed the word number of tries: {count}")
        elif func(char, word):
            for i, v in enumerate(word):
                if v == char:
                    res[i] = char
            print(f'Congratulations, this letter is in the hidden word "{"".join(res)}"')
            count += 1
        else:
            print("Try again")


        # 2 option

        # if char == word:
        #     break
        # if char not in LETTERS:
        #     print('You need to enter a letter from A to Z')
        #     continue
        # elif char in word:
        #     for i, v in enumerate(word):
        #         if v == char:
        #             res[i] = char
        #     print(f'Congratulations, this letter is in the hidden word "{"".join(res)}"')
        #     count += 1
        # else:
        #     print('There is no such letter in this word')
        # if '*' not in res:
        #     break
    print("You guessed the word right away") if not count else print(f'You guessed the word number of tries: {count}')

