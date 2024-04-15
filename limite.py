

from sympy import limit, Symbol

x = Symbol("x")
y = Symbol("y")
h = Symbol("h")




ep1 = (x**2 -25)/(x-5)
limite1 = limit(ep1,x,5)

print(limite1)


