#!/usr/bin/python

def reverse_string_recursive(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

s = "Today"
print(reverse_string_recursive(s))


