#1

numbers = input("numbers in a list: ")
listt = list(map(int, numbers.split()))
sum = 1
for i in listt:
    sum *= i
print("sum of multiply:", sum)

#2

def count_letters(sentence):
    lower = 0
    upper = 0
    for i in sentence:
        if i >= "A" and i <= "Z":
            upper += 1
        if i >= "a" and i <= "z":
            lower += 1
    print("sum of lower case:", lower)
    print("sum of upper case:", upper)

letter = str(input("soilem: "))
count_letters(letter)

#3

def palindrom(sentence):
    if sentence != sentence[::-1]:
        return f"{sentence} is not polindrom"
    else:
        return f"{sentence} is polindrom"

#4

import math
import time

time1 = int(input("milisecond: "))
time2 = int(input("milisecond 2: "))

print(f"Square root of {time1} after {time2} miliseconds is {math.sqrt(time1)}")

#5

listt = input("list numbers: ")
mylist = list(map(int, listt.split()))
print("True mylist:", all(mylist))