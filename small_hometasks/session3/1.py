import string

alpha = string.ascii_lowercase
test_strings = ['hello', 'world', 'python']

def test1_1(*args):
    ch_set = set()
    for letter in alpha:
        if all([letter in arg for arg in args]):
            ch_set.add(letter)
    return ch_set

def test1_2(*args):
    ch_set = set()
    for letter in alpha:
        if any([letter in arg for arg in args]):
            ch_set.add(letter)
    return ch_set

def test1_3(*args):
    ch_set = set()
    for letter in alpha:
        if [letter in arg for arg in args].count(True) > 1:
            ch_set.add(letter)
    return ch_set

def test1_4(*args):
    ch_set = set()
    for letter in alpha:
        if any([letter in arg for arg in args]):
            ch_set.add(letter)
    return set(alpha) - ch_set