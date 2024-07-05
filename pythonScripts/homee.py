#!/usr/bin/python

x = "Hello"
y = 23

print(bool(x))
print(bool(y))
print(isinstance(x, int))
print(isinstance(y, int))

g = 20
h = 90
if g > h:
    print("g is greater than h")
else:
    print("g is less than h")

mytuple = ("beans", "rice", "cocoyam", "eggyork", "plantain")
y = list(mytuple)
y.append("yam")
mytuple = tuple(y)
print(mytuple)





thetuple = ("mat", "cap", "tapswap", "whot")
(blue, *red, white) = thetuple
print(blue)
print(red)
print(white)

ourtuple1 = ("tree", "houses", "homes", "television")
ourtuple2 = ("men", "women", "kids")
ourtuple = (ourtuple1 + ourtuple2) * 2
print(ourtuple)


thisset = set(("one","two","three","four"))
print(thisset)

thisset.update(ourtuple)
print(thisset)

             

