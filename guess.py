a="sujan"
guess=""
count=0
l=5
while guess!=a:
    if count==l:
        print("game over")
        break
    else:
        guess=input("enter your guess :")
        count+=1

else:
    print("yes you won !!!")
    