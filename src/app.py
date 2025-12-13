import math

#basic tests

def add (a,b):
    return a+b

def subtract (a,b):
    return a-b

def multiply (a, b):
    return a*b

def division (a,b):
    if b ==0:
        raise ValueError("can't divide by zero")
    return a/b

#advanced tests

def log(a, base=10):
    if a <= 0:
        raise ValueError("log undefined for zero or negatives")
    return math.log(a, base)
    
def square(a):
    return a*a

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def sqroot(a):
    if a<0:
        raise ValueError("squart root of negative is imaginary")
    return math.sqrt(a)

#a=part, b=whole
def percent(a, b):
    if b == 0:
        raise ValueError("0 cant be split")
    return (a/b)*100
    