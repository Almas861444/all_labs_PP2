def histogram(arr):
    for i in arr:
        print("*"*i)
n=input("numbers:")
mylist=list(map(int,n.split()))
histogram(mylist)