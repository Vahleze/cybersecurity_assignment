#!/usr/bin/python

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["apple", "banana", "cherry", "guava", "pawpaw"]

print(len(x))
print(len(y))
print(type(x))
print(type(y))


print(x[1:4])
print(y[:3])

print(y[2:])
print(y[-2])
if "lemon" not in y:
    print("Lemon is not in the list y")
y[4] = "lemon"
print(y)
if "lemon" in y:
    print("lemon is in the list y")
y[1:4] = ["pear","gardenegg"]
print(y)
x.insert(3, 100)
print(x)

for i in x:
    print(i)
for i in range(len(y)):
    print(y[i])

j = 0
while j < len(x):
    print(x[j])
    j += 1

[print(k) for k in y]

todolist = ["land", "house", "gold", "enterprise", "investments"]
for i in range(len(todolist)):
    print(todolist[i])


p = 1
while p < len(todolist):
    print(todolist[p])
    p = p + 2
[print(x) for x in todolist]

newlist = []

for x in todolist:
    if "o" in x:
        newlist.append(x)
        print(newlist)

mylist =[x for x in todolist if "e" in x]
print(mylist)





    

