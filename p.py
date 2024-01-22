class A:
    def show(self):
        print("welcome")
    def show(self,name):
        print(self.name)
    def show(self,name,age):
        print(self.name)
        print(self.age)
a=A()
a.show()