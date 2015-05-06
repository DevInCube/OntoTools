import enchant

en_dict = enchant.Dict("en_US")

#@todo generate a list of errors from text and then user approves the corrections

def correct(word):
    if not en_dict.check(word):
        return en_dict.suggest(word)[0]
    return word

# bad bad
def is_english_word(word):
    if not en_dict.check(word) and len(en_dict.suggest(word)) == 0:
        return False
    return True

if __name__ == "__main__":
    print(correct('Tst'))
    print(str(is_english_word('Petite')))