#!/usr/bin/python

def palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrome_recursive(s[1:-1])
    return False

s = "rotator"
print(palindrome_recursive(s))

