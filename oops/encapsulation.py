# #encapsulation-->wrapping method and data in a unit(class)
# class Student:
#     def __init__(self) -> None:
#         self.name="sujan"
#     def show(self):
#         print(self.name)

# #it  use private and protect to restrict from globally
#         #_name (protected)
#         #__name(private)

# a=Student()
# a.name="Ram"

# class A:
#     def __init__(self) -> None:
#         print(a.name)

# b=A()

class Student:
    __name="sujan" #private
    # _age=24  #protect

    def show(self):
        print(self.__name)
        print(self._age)
a=Student()
a.show()
# print("my name is",a.__name)
print("my age is  ",a._age)

