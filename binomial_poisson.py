import matplotlib.pyplot as plt
import math as math
import tkinter
def binomial(k,n,p):
    num = math.factorial(n) * math.pow(p,k) * math.pow(1-p,n-k)
    den = math.factorial(k) * math.factorial(n-k)
    return num/den
def poisson(k,l):
    num = math.pow(l,k) * math.exp(-l)
    den = math.factorial(k)
if __name__=="__main__":# programme principal
    n = 80
    p = 0.05
    rep = []
    pbinomial = []
    ppoisson = []
    for k in range(n+1):
        pbinomial.append(binomial(k,n,p))
        ppoisson.append(poisson(k,n*p))
        rep.append(k)
    plt.plot(rep,pbinomial)
    plt.plot(rep,ppoisson)
    plt.show
