from math import sqrt
from math import pow

a = 1
b = 1 / sqrt(2)
t = 1 / 4
p = 1

print('Choose a Pi between:')
print('1. Gauss-Legendre Algorithm')
piIn = (int(input()))

if piIn == 1:
  for i in range (1,21):
      acurr = (a + b) / 2
      bcurr = sqrt(a * b)
      tcurr = t - p * pow((a - acurr),2)
      pcurr = 2 * p
      pi = pow((acurr + bcurr),2) / (4 * tcurr)
      print(str(i) + '   ' + str(pi))
      
      a = acurr
      b = bcurr
      t = tcurr
      p = pcurr