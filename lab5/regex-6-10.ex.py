import re

with open("row-6-10.ex.txt") as f:
    word = f.read()

print("Exercise 6")
matches = re.sub(r"[., ]",':',word)
print(matches)

print("Exercise 7")
matches = re.sub(r"_",'',word)
print(matches)

print("Exercise 8")
matches = re.findall("[A-Z][^A-Z]*", word)
print(matches)

print("Exercise 9")
matches = re.findall("[A-Z][a-z]*", word)
print(matches)

print("Exercise 10")
matches = re.sub(r"[A-Z]",'_', word)
print(matches)