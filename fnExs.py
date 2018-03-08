# Exercise 1
def hello(name):
    print("Hello",name)
    
hello("Maximus")

# Exercise 2
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def f(x):
    return x + 1

ys = []
xs = list(range(-3,4))


for x in xs:
    ys.append(f(x))


pyplot.plot(xs,ys)
pyplot.savefig('ex2.png')
pyplot.close()

# Exercise 3
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def g(x):
    return x**2

y_s = []
x_s = list(range(-100,101))


for x in x_s:
    y_s.append(g(x))


pyplot.plot(x_s,y_s)
pyplot.savefig('ex3.png')
pyplot.close()

# Exercise 4
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def evenOdd(num):
    if(num%2 == 0):
        return -1
    else:
        return 1
        
yS = []
xS = list(range(-5,6))
    
for x in xS:
    yS.append(evenOdd(x))


pyplot.bar(xS,yS)
pyplot.savefig('ex4.png')
pyplot.close()

# Exercise 5
import matplotlib
import math
matplotlib.use("Agg")
from matplotlib import pyplot

def h(x):
    return math.sin(x)
    
    
Ys = []
Xs = list(range(-5,6))

for x in Xs:
    Ys.append(h(x))
    
pyplot.plot(Xs,Ys)
pyplot.savefig('ex5.png')
pyplot.close()

# Exercise 6
import matplotlib
import math
import numpy
matplotlib.use("Agg")
from matplotlib import pyplot
from numpy import arange

def h(x):
    return math.sin(x)
    
    
Ys = []
Xs = arange(-5,6,0.1)

for x in Xs:
    Ys.append(h(x))
    
pyplot.plot(Xs,Ys)
pyplot.savefig('ex6.png')
pyplot.close()

# Exercise 7
import matplotlib
import math
import numpy
matplotlib.use("Agg")
from matplotlib import pyplot
from numpy import arange

def F(c):
    return 1.8*c+32
    
    
f = []
c = arange(0,101,1)

for x in c:
    f.append(F(x))
    
pyplot.plot(c,f)
pyplot.savefig('ex7.png')
pyplot.close()

# Exercise 8
def TorF():
    answer = input("Do you want to play again (Y on N)?")
    if(answer.upper() == 'Y'):
        return True
    else:
        return False
TorF()

# Exercise 9
def YorN():
    response = input("Do you want to play again (Y on N)?")
    while (response.upper() != 'Y' and response.upper() != 'N'):
        print("Invalid Input!")
        response = input("Do you want to play again (Y on N)?")
    if(response.upper() == 'Y'):
        return True
    elif(response.upper() == 'N'):
        return False
YorN()