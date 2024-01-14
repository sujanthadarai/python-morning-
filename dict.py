#dict - key value pairs,order ,mutable
a={
    "name":"ram",
    "age":24,
   
}
print(type(a))

print(a["name"])
print(a.get("name")) #it help to access data direct
print(a.values())
print(a.keys())
print(a.items())

#add
a["email"]="sujanthadarai710@gmail.com"
#delete
# del a["email"]
# a.pop("name")
# a.popitem()
b={
    "course":"python",
    "age":25
    
}
a.update(b)
print(a)
