#expection handling-->it is responsible of finding event occur in program run ,an expection handle that error with out crash other code

# Syntax:
# try:
#     #code 
# except:
#     #code for error occur


# try:
#     a=int(input("enter your any number :"))
#     b=int(input("enter your any number :"))


#     def show(a,b):
#         s=a/b
#         # str1="sujan"  
#         # print(str1[7])  #it gives index error
#         print("sum of a and b is ",s)

#     show(a,b)
# except IndexError:
#     print("you have to give exists index")

# except ValueError:
#     print("you have to put both int number")
# except ZeroDivisionError:
#     print("you cannot divide by zero")


# finally:
#     print("always excuted")
num=int(input("enter your number"))

def show(num):
    try:
        s="sujan"
        print(s[9])
        return num
    except:
        print("this is for error")
        return 0
    finally:
        print("this is imp code ")

show(num)
print("our imp code")

    