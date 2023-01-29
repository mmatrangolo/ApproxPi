from math import sqrt
from math import pow
import random

from decimal import *
from decimal import localcontext

def gauss_legendre_approx_pi():
  # Tell Python to use Decimal inside this block. 
  # Decimal is type allowing to use numbers with arbitrary precision.
  with localcontext() as ctx:
    ctx.prec += 1

    # Initial values
    a = 1
    b = 1 / Decimal(2).sqrt()
    t = 1 / Decimal(4)
    p = 1

    # Current and previous pi values
    pi    = None
    piOld = None

    # Num of required iterations
    n = 0

    # Stop when pi and piOld are equals that means that the 
    # digits of pi are accurate up until the amount of printed 
    # digits because from that point on the algorithm will keep
    # producing the same value of pi.
    while pi == None or pi != piOld:
      n += 1 # Increment the num of total iterations required

      an = (a + b) / 2
      b = (a * b).sqrt()
      t -= p * (a - an) * (a - an)
      a, p = an, 2 * p

      piOld = pi
      pi = (a + b) * (a + b) / (4 * t)

  print("Needed iterations = " + str(n))
  return pi

def montecarlo_approx_pi(n):
  inside = 0 # number of dots in the circle
  total  = 0 # total number of events

  # Execute n experiments
  while total <= n:

    # Generating random dots with coordinates between -1 and 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Increment the 'inside' counter if the dot landed in the circle
    if sqrt(x**2 + y**2) <= 1:
      inside += 1

    total += 1

  # Calculate pi from the prob of dot landing in the cirlce
  pi = 4 * (inside / total) 

  return pi

print('Choose a Pi between:')
print('')
print('1. Gauss-Legendre Algorithm')
print('2. Monte Carlo Algorithm')
print('')
piIn = (int(input()))

if piIn == 1:
  print('')
  print('How many digits would you like to calculate?')
  print('')
  precision = int(input())
  print('')

  getcontext().prec = precision
  print(str(gauss_legendre_approx_pi()))

if piIn == 2:
  print("pi =" + str(montecarlo_approx_pi(100000000)))