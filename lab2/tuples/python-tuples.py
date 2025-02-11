#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#6
tuple1 = ("abc", 34, True, 40, "male")
#7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)