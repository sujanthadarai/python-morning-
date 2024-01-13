# 2.Get all values from the dictionary and add them to a list but don’t add duplicates

a={
    "name":"sujan",
    "age":24,
    24:24
}
b=a.values()
b=set(b)
print(list(b))
