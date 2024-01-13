#sissor ,papper rock
a="Welcome to Sipalaya info tech Game"
print(a.center(70,"-"))
b='''
   S for Sissor,
   P for Papper,
   R for rock

'''

print(b)
print("Remember!!! S>P, P>R and R>S")
user=input("enter your choice : \n ")
user=user.upper()
print(f" Your choice is {user}")

import random
computer=random.choice(['S','P','R'])
print(f" computer choose {computer}")

if (user=='S' and computer=='P') or (user=='P' and computer=='R') or \
    (user=='R' and computer=='S'):
        print("You won !!!")
        
elif user==computer:
    print("Draw!!!")

elif user not in ['S','P','R']:
    print("keyward is wrong !!!")
    
else:
    print("computer won!!!")


