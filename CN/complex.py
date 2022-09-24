class complex:
    def __init__(self, one, other):
        self.one=one
        self.other=other
    def add(self, otherObj):
        self.one=self.one+otherObj.one
        self.other=self.other+otherObj.other
    def print_res(self):
        print(f"Real part is: {self.one}, Imigirnary part is: {self.other}")

s=complex(4,5)
s1=complex(5,4)
s.add(s1)
s.print_res()
