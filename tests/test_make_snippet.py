import pytest
from lib.make_snippet import *

"""""

Test-drive a function with the following design:

Design

A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.
You may immediately think "I know how to code that!". Resist that temptation and stick to the test-driving process.

Write a small example as a test.
Run the test (RED).
Write enough code to make that test pass.
Run the test (GREEN).
Refactor if necessary.
Return to step 1 and keep going until your program is complete.

"""

"""
Test if dots have been added after more than five words
"""

def test_if_dots_have_been_added_after_the_first_five_words():
    result = make_snippet("This is a place where I capture all of my thoughts")
    assert result == "This is a place where"

"""
Test that no dots are added if less than five words
"""

def test_no_dots_added_if_less_than_five_words():
    result = make_snippet("Fatma's Diary")
    assert result == "Fatma's Diary"

"""
Test that an error is thrown if nothing is written
"""

def test_no_words_error():
    result = make_snippet()
    with pytest.raises(Exception) as e:
        error_message = str(e.value)
    assert error_message == "Error, diary is empty"