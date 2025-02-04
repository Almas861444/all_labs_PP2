def permutations(some):
    n = len(some)

    for i in range(n):
        for j in range(n):
            print(some[(j-i)], end =" ")
        print()
k = str(input("word:"))
permutations(k)