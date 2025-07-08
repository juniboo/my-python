from math import sqrt
from operator import add,mul,sub
def div(a,b):
       return a/b

def improve(update,close,guess=1):
       while not close(guess):
             guess=update(guess)
       return guess
def approx_eq(x,y,tolerance=1e-7):
       return abs(x-y)<tolerance
def newton_update(f,df):
       def update(guess):
              return guess-f(guess)/df(guess)
       return update
def newton_close(f):
       def close(guess):
              return approx_eq(f(guess),0)
       return close
def newton(f,df):
       return improve(newton_update(f,df),newton_close(f))
def f(x):
       return x**3+x**2+x+1-sqrt(2)
def df(x):
       return 3*x*x+2*x+1
print(newton(f,df))
