import re

with open("row-1-5-ex.txt") as f:
    word = f.read()

print("Exercise 1")
matches = re.findall("a.*b", word)
print(matches)

print("Exercise 2")
matches = re.findall(r"ab{2,3}", word)
print(matches)

print('Exercise 3')
matches = re.findall("[a-z]_+[a-z]+", word)
print(matches)

print('Exercise 4')
matches = re.findall(r"[A-Z][a-z]+", word)
print(matches)

print('Exercise 5')
matches = re.findall(r"a+.b", word)
print(matches)