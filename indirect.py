class A:
    def A(self):
        print('Method of A')

class B(A):
    def B(self):
        print('Method of B')

class C(B):
    def C(self):
        print('Method of C')
obj = C()
obj.A()
obj.B()
obj.C()