### about recursion
def sum_naturals(n):
    k,total = 1,0
    while k<=n:
        k,total = k+1,total+k
    return total
print(sum_naturals(4))
def sum_squares(n):
    k,total = 1,0
    while k<=n:
        k,total = k+1,total+k*k
    return total
print(sum_squares(4))
def sum_cubes(n):
    k,total = 1,0
    while k<=n:
        k,total = k+1,total+k*k*k
    return total
print(sum_cubes(4))
### improved method for sum
def sum(n,term):
    k,total = 1,0
    while k<=n:
        k,total = k+1,total+term(k)
    return total
def cube(n):
    return n**3
def sum_cubes_improved(n):
    return sum(n,cube)
print(sum_cubes_improved(4))
### next level
from operator import mul,add
def make_adder(x):
    def adder(y):
        return x+y
    return adder
r = make_adder(3)
print(r(3))
def make_adder_plus(x):
    def f(y):
        def g(z):
            return x+y+z
        return g
    return f
print(make_adder_plus(3)(4)(5))
def play(x,y,z):
    return x*y+y*z+x*z

def curry3(f):
    def g(x):
        def h(y):
            def p(z):
                return f(x,y,z)
            return p
        return h
    return g
q = curry3(play)
print(q(1)(2)(3))
def composel(f,g):
    def h(x):
        return f(g(x))
    return h
w = composel(cube,make_adder(2))
print(w(1))
def nest(x,f):
    return f(f(x))
print(nest(2,cube))

