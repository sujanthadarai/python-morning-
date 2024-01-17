# fundamental concept
#inheritance-->class that contain another class that share method and attributes
#code reuse
# parent--->base class

# child--->derived class

# class A:  #parent class  #child class
#     def show1(self):
#         print(" this is function1")

# class B(A):
#     def show2(self):
#         print("thi is function2")

# class C(B):
#     def show3(self):
#         print("this is function3")
# # Single level inheritance   A-->B--C

# b=B()
# b.show2()
# b.show1()

# c=C()
# c.show1()
# c.show2()

# c.show3()

#multiple inheritance  A , B -->C
class A:
    def show(self):
        print("this is function1")
class B:
    def show(self):
        print("this is function2")

class C(A,B):
    def show(self):
        print("this is functin3")
a=C()
a.show1()
a.show2()
a.show3()
    

