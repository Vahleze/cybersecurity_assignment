#!/usr/bin/python

import sys

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "An Exception ocuurs"
    finally:
        print("No exception")

def main():
    argv = sys.argv
    if len(argv) != 3:
        print("Error: usauge ./filename num1 num2")
        return 0
    print(div(int(argv[1]), int(argv[2])))
    return 0

if __name__ == "__main__":
    main()
