#!/usr/bin/python
import sys

def main():
    argv = sys.argv

    if len(argv) != 4:
        print("Error: Usuage ./filename Ass1 Ass2 Exam")
        return -1 

    Ass1 = int(argv[1])
    Ass2 = int(argv[2])
    Exam = int(argv[3])
    x = (Ass1 + Ass2 + Exam)
    
    
    if x >=70 and x <= 100:
        print("Your score grade is A")
    elif x >= 60 and x <= 69:
        print("Your score grade is B")
    elif x >= 50 and x <= 59:
        print("Your score grade is C")
    elif x >= 40 and x <= 49:
        print("Your score grade is D")
    elif x <= 39:
        print("Your score grade is F")
    else:
        print("No result")



if __name__ == "__main__":
    main()
