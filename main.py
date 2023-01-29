from math import sqrt
from math import pow
import random



def glpi(n):

  print('')

  a = 1
  b = 1 / sqrt(2)
  t = 1 / 4
  p = 1
    
  for i in range (1, n + 1):
    acurr = (a + b) / 2
    bcurr = sqrt(a * b)
    tcurr = t - p * pow((a - acurr), 2)
    pcurr = 2 * p
    pi = pow((acurr + bcurr), 2) / (4 * tcurr)
    print(str(i) + '   ' + str(pi))
    
    a = acurr
    b = bcurr
    t = tcurr
    p = pcurr

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
  print('How many Iterations would you like to calculate?')
  print('')
  iter = int(input())
  print('')
  glpi(iter)

if piIn == 2:
  print("pi =" + str(montecarlo_approx_pi(100000000)))