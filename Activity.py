class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            return "ob1<ob2"
        else:
            return "ob1>ob2"
    def __eq__(self, other):
        if (self.a==other.a):
            return "both are  equal"
        else:
            return "they are not equal "
ob1=A(3)
ob2=A(4)
print(ob1<ob2)
ob3=A(4)
ob4=A(4)
print(ob3==ob4)