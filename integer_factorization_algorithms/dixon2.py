from gmpy2 import isqrt,gcd,next_prime, is_prime
import sys
import bitarray

def dixon(N,B=7,explain=False):

  if is_prime(N):
    return N,1

  start = isqrt(N)

  if (start ** 2) == N:
    return start,start

 

  def primes(B):
    p = 1
    tmp = []
    while p < B:
      tmp.append(p)
      p = next_prime(p)
    return tmp

  base = primes(B)
  lqbf = pow(base[-1],2)+1
  QBF = bitarray.bitarray(lqbf)
  
  i = start

  basej2N = []
  for j in range(0,len(base)):
    p = pow(base[j],2,N)
    basej2N.append(p)
    QBF[p] = 1

  while i < N:
    i2N = pow(i,2,N)
    if i2N < lqbf and QBF[i2N] == 1:
      for k in range(0,len(base)):
        if QBF[basej2N[k]] == 1:
          #if i2N == basej2N[k]:
          f=gcd(i - base[k],N)
          if explain:
            print("%d = pow(%d,2,n)" % (i2N,i))
            print("%d = pow(%d,2,n)" % (basej2N[k],base[k]))
            print("%d - %d = %d" % (i,base[k],f))
          if 1 < f < N:
            return f,N//f
    i+=1
  return -1

print(dixon(int(sys.argv[1]),B=int(sys.argv[2])))
