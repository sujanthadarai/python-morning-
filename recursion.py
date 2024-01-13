#recursion function _function shouldonot call by ourself, it call itself

def fact(num):
    if num==0:
        return 0

    elif num==1:
        return 1
    return num* fact(num-1)

num=int(input("enter  your number :"))
print(fact(num))

# lambda -anonmyus function


