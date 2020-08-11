#write a function to determine if a given string is a palindrome
#regular expression module in python
import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards
