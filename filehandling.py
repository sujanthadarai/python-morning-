# file handling
# file---file is collection of data and informtion  store in a disk permanently
#file
#text file--used to store in form of characterm 
#binary file-->used to store in form of byte 


#store data:file handling ,database

#file handling---use to perform a funtion such as create,read,write,update,append

# sytax:
# open()
# #statemtn operation for file handling
# close()

#mode -->purpose of open file
#x--create
#r=read
#mode=write
#append=a

# f=open("msg.txt","r+")
# # a=f.readlines()
# # a=f.readlines()
# # f.write("this is our file\n")
# f.write("this is me")
# f.write("sujan")

# print(a)

#varaible
# f=open("msg.txt","r")
# print(f.name)
# print(f.mode)
# print(f.buffer)
# print(f.encoding) #cp1552
# print(f.closed)

#method
# f=open("msg.txt","r")
# a=f.writable()
# print(a)

# file close
# try:
#     f=open("msg.txt","r")
#     f.write("hi ")
#     f.close()
# except:
#     print("w lekhnai paro")
# finally:
#     f.close()
# print("this is most imp code")
# print(f.closed)

#with statement
with open("msg.txt","w") as f:
    f.write("hi this me")
    

# print()
print(f.closed)

#tell()
#seek()















