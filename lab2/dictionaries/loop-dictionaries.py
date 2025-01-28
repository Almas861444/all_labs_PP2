thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#1
for x in thisdict:
    print(x)
  
#2s
for x in thisdict:
    print(thisdict[x])
#3
for x in thisdict.values():
    print(x)
#4
for x in thisdict.keys():
    print(x)
#5
for x, y in thisdict.items():
    print(x, y)