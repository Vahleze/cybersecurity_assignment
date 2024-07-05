#!/usr/bin/python
import sys


def revStr1(str):
    i = str[::-1]
    print(i)

    




def main():
    argv = sys.argv
    if len(argv) != 2:
        print("Error: usage: ./filename str")
        return -1
    str = argv[1]
    revStr1(str)
    return 0




if __name__ == "__main__":
    main()
    
