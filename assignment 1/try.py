class Arbitrary(object):
    def __init__(self, data=1): self.data = data
    def getit(self): return self.data * 2
    class Thing(Arbitrary): 
        def __init__(self, value=3): super().__init__(value * 2)
        a, b = Arbitrary(2), Thing()
        print(a.getit(), b.getit())
