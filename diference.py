class Difference:
    def __init__(self, a):
        self.__elements = a


        # Add your code here
    def computeDifference(self):
        dif = 0
        minim = min(self.__elements)
        maxim = max(self.__elements)

        dif = maxim - minim
        self.maximumDifference=dif


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)