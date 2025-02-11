def palindrom(text):
    if text==text[::-1]:
        print("YES")
    else:
        print("NO")

text = input("text: ")
palindrom(text)