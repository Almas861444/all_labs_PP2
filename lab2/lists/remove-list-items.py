#1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#6
thislist = ["apple", "banana", "cherry"]
del thislist
#7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)