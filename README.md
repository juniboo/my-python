                                                                     issue 1:
📕 Newton-raphson Methond in python
📌 Introduction:The Newton-Raphson method is a powerful and widely-used numerical technique for finding roots of a real-valued function. It uses both the value and the derivative of a function to quickly converge to a solution.

This project demonstrates a basic Python implementation of the method. It helps me reinforce my understanding of Python functions, loops, precision control, and mathematical thinking.
🧠 Concept:

The Newton-Raphson formula is: x(n+1)=x(n)-f(x(n))/df(x(n)) or Look here  https://latex.codecogs.com/png.image?\dpi{150}&space;x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}


You start with an initial guess and iterate this formula until the result stabilizes (i.e., the difference between steps is very small)



💡Sample Code:Solving a complex cubic equation:
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
💡💡Thus we can derive the general formula
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
💡💡💡Extension:
We can find the nth root based on Newton's iteration method
Let't start with the square root
A quadratic eqation:f(x)= x**2-a
According to the mathematical principle of Newton's iteration method:
x(n+1)=(xn+a/xn)/2
so we do the following:
#利用牛顿迭代法求二次方根:
def average(x,y):
       return (x+y)/2
def sqrt_average(x,a):
       return average(x,a/x)
def improve(update,close,guess=1):
       while not close(guess):
              guess= update(guess)
       return guess
def approx_eq(x,y,tolerance=1e-3):
       return abs(x-y)<tolerance
def sqrt(a):
       def sqrt_update(x):
              return average(x,a/x)
       def sqrt_close(x):
              return approx_eq(x*x,a)
       return improve(sqrt_update,sqrt_close) 
print(sqrt(4),sqrt(5),sqrt(6))

💡💡💡💡And so on to the nth root:
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-7):
    return abs(x - y) < tolerance

def newton_update(f, df):
    def update(guess):
        return guess - f(guess) / df(guess)
    return update

def newton_close(f):
    def close(guess):
        return approx_eq(f(guess), 0)
    return close

def newton(f, df):
    return improve(newton_update(f, df), newton_close(f))

# ✅ 通用的 n 次方根函数，基于 Newton 法
def nth_root(a, n):
    def f(x):
        return x**n - a
    def df(x):
        return n * x**(n - 1)
    return newton(f, df)


