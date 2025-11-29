"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


# Fixed the repeat_string function above so that it passes the failing test
def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


# Fixed the failing is_long_word function
def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Assert statements to show if Car sets the fuel correctly
    car = Car(fuel=10)
    assert car.fuel == 10

    car = Car()
    assert car.fuel == 0


# Write and test a function to format a phrase as a sentence,
def phrase_to_sentence(phrase):
    """
    Format phrase as sentence: start with capital, end with full stop
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('haLLo WeLT')
    'Hallo welt.'
    """
    if not phrase:
        return ""
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

# Uncommented the following line and run the doctests
doctest.testmod()

