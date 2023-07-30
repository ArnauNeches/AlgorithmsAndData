#I will check the time of execution of some function using the time module

import time

def sum_of_n(n):
    s = time.time()
    res = 0
    for i in range(1, n+1):
        res += i
    t = time.time()-s
    print(f"The sum of the {n} first numbers is {res} and it took {t:.15f} seconds")

#Now using a formula we'll see that it takes less

def sum_of_n2(n):
    s = time.time()
    res = (n*(n+1))/2
    t = time.time()-s
    print(f"The sum of the {n} first numbers is {res} and it took {t:.15f} seconds")

sum_of_n(10000000)
sum_of_n2(10000000)

