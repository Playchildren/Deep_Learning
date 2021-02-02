"""
尽量定义行矩阵和列矩阵 而不是 rank 1 array
多多使用assert和reshape函数来确保矩阵规格的正确性
"""

import numpy as np

# dis-commend way
a = np.random.randn(5)

print(a)

print(a.shape)      # (5, )秩为1的数组 rank 1 array

print(a.T)

print(np.dot(a, a.T))

# commend way
a = np.random.randn(5, 1)

print(a)

print(a.shape)

print(a.T)

print(np.dot(a, a.T))

assert (1 == 1)
# assert (1 == 2)
# 可以用此方法检验矩阵的shape是否我们需要的

# 或者重新定义
a = a.reshape(5, 1)
