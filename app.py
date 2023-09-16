from game import get_guess_word, guess, get_photos


from constants import LIST_WORDS,  PICTURE_DICTIONARY


def app():
    word = get_guess_word(LIST_WORDS)
    get_photos(PICTURE_DICTIONARY, word)
    guess(word)


app()
