#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
  print(x)

#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      break
  print(x)