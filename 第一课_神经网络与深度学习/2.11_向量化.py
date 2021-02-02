# To avoid using for loop in model, we use Vectorization to simplify the expression.
# Parallelism 充分利用了并行化运算, GPU performs better than CPU
import numpy as np
import time

a = np.array([1, 2, 3, 4])      # create an array
print(a)

# ----- Vectorization Version -----
a = np.random.rand(1000000)     # create a million dimensional array by random numbers

b = np.random.rand(1000000)     # as same as array_a

time0 = time.time()             # read time before run next step
c = np.dot(a, b)                # Array_a times Array_b
time1 = time.time() - time0     # read time used by np.dot
print(c)
print(f"Vectorization use {time1*1000}ms")      # print

# ----- non-Vectorization Version -----
c = 0
time0 = time.time()             # read time before run next step

for i in range(1000000):        # do same function used by for loop
    c += a[i] * b[i]

time1 = time.time() - time0     # read time used by for loop
print(c)
print(f"Vectorization use {time1*1000}ms")      # print
