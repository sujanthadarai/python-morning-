#while loop
# a=10
# while a<10:
#     print(a)   
#     a+=1

#infinity loop 
# while True:
#     print("hello world")
    


#condition statetment
 #break 
a=1
while a<10:
    
    a+=1
    if a==5:
        continue
    print(a)
    
    
    
    
#continue
# for i in range(10):
#     if i%3==0:
#         continue
#     print(i)

# for i in range(10):
#     pass


a="sujan"
guess=""
c=0
l=5
while guess!=a:
    if c==l:
        print("game over")
        break
    else:
        guess=input("Enter your guess ")
    c+=1
else:
    print("Yes you won!!!")
    

    