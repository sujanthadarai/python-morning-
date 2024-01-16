#instance & class variable/static
#instance variable is a variable whose separate copy of creating every object
#instancevaraible access instance method which contain self parameter in it first argument
 
class Student:
    school="united"
    def __init__(self,name): 
        self.name=name #instance variable
    
    def show(self):  #instance method
        print(self.name) #instacne varaible access inside class
a=Student("sujan")
a.name="Ram"  #instance variable access outside the class  -->objectName.instance variable
a.show()


b=Student()
b.show()

#class variable -->variable whose have single copy of every object
#class method -->acces classs varraible with cls in first argument
class Student:
    school="mangala"
    def __init__(self):
        self.name="sujan"  

    @staticmethod  #decorater
    def show():  #class method
        print("print") #class varible acces inside class

a=Student()
Student.school ="united"
a.show()   

b=Student()
b.show()


        
        

        