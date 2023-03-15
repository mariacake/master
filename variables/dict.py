#dict = {1, 5, 7, 'a', 'rge', 1+3j, None}
#print(dict)

dict = {"name":"Maria", "sex":"F", 2: [1, 2, 3], 3: "abc", (1, 2, 3): {"Age": 28, 13: 69}, 3: "abnnnn"}

print(dict, type(dict))
print(dict[3])

dict["country"] = "romania"
print(dict["country"])
print(dict)

del dict[2]
print(dict.keys())
print(dict.values())
print(dict.items())

print("are" in "ana are mere")
print(10 in [1, 10])
print(10 in (1, 10))
print("name" in {"name":"Maria", "age":23})
print("Maria" in dict)

dict = {"name":"Maria", "sex":"F", 2: [1, 2, 3], 3: "abc", (1, 2, 3): {"Age": 28, 13: 69}, 3: "abnnnn"}

print(dict.get("sexy", 10))

seti = {}
print(type(seti))

#set = set()
#set = {1, 3, 'maria', 'frumoasa', True, True, False}
#print(type(set))
#print(set, type(set))

print(hash(True))

set = set()
set = {1, 2, 3,4 ,5 ,6,7,8,9, 10}

set.pop()
print(set, type(set))
print(len(set))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(type(set1))

li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]

print(li1 + li2)

