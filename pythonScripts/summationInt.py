#!/usr/bin/python
import sys


def numSummation(n):
    n = int(input("Enter a number"))
    total = sum(range(n+1))
    print(f" The summation from 0 to {n} is: {total}")







def main():
    argv = sys.argv
    if len(argv) != 2 :
        print("Error: usage: ./filename str")
        return -1
    str = argv[1]
    numSummation(5)
    return 0


if __name__ == "__main__":
    main()
