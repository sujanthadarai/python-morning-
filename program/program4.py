# 3.Remove duplicates from a list and create a tuple and find the minimum and maximum number
a=[9,2,2,2,3,3,3,4,5,5]
a=set(a)
a=tuple(a)
b=a[len(a)-1]
print(b)