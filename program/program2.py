# Create a list by picking an odd-index items from the first list and even index items from the second
# in one third list 

a=[1,2,3,4,5]
b=[6,7,8,9,10]
e=[]
e.extend(a[0::2]+b[1::2])
print(e)