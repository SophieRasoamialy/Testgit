import math
class Complexe:
    def module(a,b):
        return math.sqrt(a**2 + b**2)
    def argument(a,b):
        sin = a/module(a,b)
        cos = a/module(a,b)
        tag = sin/cos
        return math.atan(tag)
    def coordo_polaire(a,b):
        coordo = [module(a,b), argument(a,b)]
        return coordo
    def conjugaison(a,b):
        print(a,"-i",b)
    def __add__(self,a):
        return a
    def __radd__(self, a):
        return a
    def __sub__(self,a):
        return a
    def __rsub__(self,a):
        return a
    def __mul__(self,a):
        return a
    def __rmul__(self,a):
        return a
        
