class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def ret(self):
        print(self.m1)
    def __add__(self,other):
        m1=self.m1 +other.m1
        m2 =self.m2+other.m2
        return m1+m2
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1 = student(40,60)
s2 = student(50,70)
print(s1+s2)
print(s1)