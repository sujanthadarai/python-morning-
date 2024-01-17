#mro-->he set of rules that construct the linearization
class A:
    def __init__(self) -> None:
        # super().__init__()
        print("this is A init")

class B:
    def __init__(self) -> None:
        # super().__init__()
        print("this is B init")

    
class C(B,A):
    def __init__(self):
        super().__init__()  #it help to print both 
        print("C is init")
a=C()   #paila afno init contructron herxa xaina vani class A ko init print garxa 