import pytest
from palindrome import longest_palindromic_substring as palindrome

# Test common inputs
def test_common_inputs():
    assert palindrome("babad") == "bab"
    assert palindrome("cbbd") == "bb"

# Test edge cases
def test_single_letter_case():
    assert palindrome("a") == "a"

def test_two_letter_case():
    assert palindrome("ac") == "a"

def test_empty_string():
    with pytest.raises(ValueError):
        palindrome("")

def test_long_string():
    assert palindrome("racecar") == "racecar"