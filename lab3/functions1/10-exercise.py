def unique(mylist):
    result = []
    for i in mylist:
        if mylist.count(i) == 1:
            result.append(i)
    return result

n = int(input("n: "))
mylist = []
for i in range(n):
    number = int(input("number: "))
    mylist.append(number)
print(unique(mylist))