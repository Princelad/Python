"""
Module for string manipulation utilities.
"""

def reverse_string(text):
    """Reverse the characters in a string."""
    return text[::-1]

def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def capitalize_words(text):
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in text.split())
