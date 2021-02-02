# EXP ^ num

import numpy as np
import math
import time

# ----- non-Vectorization Version -----
v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
u = np.zeros((20, 1))                           # create a zero 矩阵 20x1
time0 = time.time()
for i in range(20):
    u[i] = math.exp(v[i])
time1 = time.time() - time0
print(time1*1000)

# ----- Vectorization Version -----
time0 = time.time()
u = np.exp(v)
time1 = time.time() - time0
print(time1*1000)

# ----- More Functions -----
# np.log() log值
# np.abs() 绝对值
# np.maximum() 最大值
# v**2 计算平方; 1/v 求倒数
