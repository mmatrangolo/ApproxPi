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



def mcpi():
 
  INTERVAL = 3000
 
  circle_points = 0
  square_points = 0

  for i in range(INTERVAL**2):

    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
 
    origin_dist = rand_x**2 + rand_y**2
 
    if origin_dist <= 1:
        circle_points += 1
 
    square_points += 1
 
    pi = 4 * circle_points / square_points
 
  print("Final Estimation of Pi=", pi)



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
  print('')
  mcpi()