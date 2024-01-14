#oops 
#1.procedure
#oops --->variable haru lai real world entitiy match garxa
#oops is used class and object lai use garxa

#class -->blueprint of object or collection of object
#object -->instance of class


# StudentForm ---class[blueprint]
# Ram -->ram koi nformation  --object
# sujan-->sujan ko information --object[instance]
# syam-->syam ko informtion --

#class -->group of attribute and method
#attribute=represent variable which hold data
#method -->similar to funtion,perform a action or task

# sytax:
# class ClassName:  #class
#     def __init__(self): #method
#         self.variable_name="sujan"#attribute
#         self.variable_age=24
#     def show(self):
#         #body of code
# a=ClassName()  #object
# a.show()

# class Student:
#     def __init__(self,name):
#         self.n=name
#     def show(self,age):
#         print(f"my name is {self.name} and age is {age}")
# a=Student("sujan")
# a.show(24)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"my name is {self.name}, my age is {self.age}")

# a=Student("ram",27)
# print(id(a))
# a.show()

# b=Student("sujan",24)
# print(id(b))
# b.show()

# c=Student("ram",27)
# print(id(c))
# c.show()

#Shop 
#sytax
# assert condtion, error message
class Shop:
    bonus=0.10 
    def __init__(self,name,price,qty):
        #validation
        # assert qty>=0 , f"quantity {qty} should be greater than zero"
        # assert price>=0 , f"price {price} should be greater than zero"

        self.name=name
        self.price=price
        self.qty=qty
    def Totalprice(self):
       a=12
       return self.price*self.qty*self.bonus
    
obj1=Shop("book",200,9)
print(obj1.Totalprice())

obj2=Shop("pen",10,12)
print(obj2.Totalprice())





