# #for loop 
# for i in range(10,0,-1):
#     print(i)
#     if i==1:
#         print("Go")
        
# #multiplication table 
# num=int(input("Enter the number : "))

# for i in range(1,11):
#     product=i*num
#     print(f" {num} X {i} = {product}")


# a=[2,3,4,5]
# b=[]

# for i in a:
#     b.append(i+2)
# print()

# *
# * *
# * * *
# * * * *
# * * * * *


color=["blue", "yellow", "green"]
for i in color:
    print(i, end=" ")
    for j in i:
        print(j)

n=int(input("enter your number"))

for i in range(n):
    for j in range(i):
        print("" ,end=" ")
    print()
        

