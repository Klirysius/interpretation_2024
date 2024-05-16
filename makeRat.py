import math


class MakeRat:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.calc()

    def calc(self):
       gcd = math.gcd(self.n, self.d)
       self.n /= gcd
       self.d /= gcd

    def getN(self):
        return self.n

    def getD(self):
        return self.d


M = MakeRat(6, 8)
print(M.getN(), M.getD(), M.getSum())
