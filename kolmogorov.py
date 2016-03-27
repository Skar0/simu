from __future__ import division
from scipy.stats import norm
import scipy.stats as stats
import math

#We have 1M Pi decimals

n = 1000000

piDecimals = [0 for x in range(n)]

i = 0
with open("assets/pi6.txt") as file:
    next(file)
    for line in file:
        j=0
        while j<50:
            piDecimals[i] = int(line[j])
            i += 1
            j += 1

(mu, sigma) = norm.fit(piDecimals)

d_n = stats.kstest(piDecimals,'norm',(mu,sigma),n)[0]

d_alpha = (1/float(1.2239))*(1/(6*math.sqrt(n)))

print(d_n)
print(d_alpha)
