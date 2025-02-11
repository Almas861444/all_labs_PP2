#1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]