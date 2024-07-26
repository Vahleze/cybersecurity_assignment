#!/usr/bin/python

f = open("filehandling.txt")
g = open("../../Documents/mytext.txt", "rt")
#print(f.read(3))
#print(g.readline())
for x in f:
    print(x)


#appending to an existing file    
f = open("filehandling.txt", "a")
f.write("Now we've appended and added more content to this file")
f.close()

f = open("filehandling.txt", "r")
print(f.read())



#overwriting the content of a file
f = open("filehandling.txt", "w")
f.write("Oops I've deleted the original content of this file")
f.close()

f = open("filehandling.txt", "r")
print(f.read())


z = open("thisfile.txt", "a")
z.write("This is the content of this file. Skrrrr!!!")
z.close()

z = open("thisfile.txt", "r")
print(z.read())
