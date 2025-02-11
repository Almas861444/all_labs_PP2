#1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)