# #formate string

# a=3.3333
# print(f"My name is {a:.2f}")

# name="sujan"
# age=24
# print("my name is %s and i m %d years old" %(name,age))
# name="sujan"
# print(name.center(50,"-"))
# print(name.isprintable())

# l="sujan "
# print(l.isprintable())

import re
a="my name   \n  is  sujan "
v=re.sub(r'\s+',"",a)
print(v)

