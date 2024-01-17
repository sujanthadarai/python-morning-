#polymorphism-->poly --many  morphism-form
#one thing different form 

# a="sujan"
# b=[1,2,3,4]
# print(len(b)) #len()

#duck type  --->
# class Me:
#     def show(self):
#         print("this is me")
# class You:
#     def show(self):
#         print("this is you")
# def display(var):
#     var.show()


# a=Me()
# b=You()
# display(a)
# display(b)


#method overloading
#class contain more than one method that can be same name but different parameter
# class Student:
#     def __init__(self,name='',age=''):
#        self.name=name
#        self.age=age
       

#     def show(self):
#         print(self.name)
#         print(self.age)
# a=Student("sujan",23)   
# a.show()

# class Student:
#     def sum(self,a=None,b=None):
#         s=a
#         if a!=None and b!=None:
#             s=a+b
#         elif b!=None and a==None:
#             s=b
#         elif b==None and a!=None:
#             s=a
#         else:
#             s=3
#         return s
# var=Student()
# print(var.sum())




#method overriding
class A:
    def show(self):
        print("this is me")
class B(A):
    def show(self):
        # super().show()
        print("this is you")
a=B()
a.show()