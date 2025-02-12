#1
def sqare_generator(n):
    listt = []
    for i in range(n):
        k = (i + 1)**2
        listt.append(k)
    return listt

n = int(input("Number: "))
result = sqare_generator(n)

for num in result:
    print(num)

#2
def even_numbers(n):
    listt = []
    for i in range(n):
        if i % 2 == 0:
            listt.append(i)
    return listt

n = int(input("num: "))
result = even_numbers(n)
print(result)

#3
def num(n):
    listt = []
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            listt.append(i)
    return listt

n = int(input("Num: "))
result = num(n)
print(result)

#4
def squares(a, b):
    listt = []
    for i in range(a, b + 1):
        k = i**2
        listt.append(k)
    return listt

j = int(input("Num1: "))
t = int(input("Num2: "))
result = squares(j, t)
print(result)

#5
def reversee(n):
    listt = []
    for i in range(n, 0, -1):
        listt.append(i)
    return listt

n = int(input("Num: "))
result = reversee(n)
print(result)