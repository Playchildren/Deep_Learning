"""
1.1 create a sigmoid function
"""

import math
import numpy as np


def math_sigmoid(x):
    s = 1/(1+math.exp(-x))
    return s
print(math_sigmoid(0))


x = np.array([1, 2, 3])
print(np.exp(x))
print(x+3)


def np_sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s
x = np.array([1, 0, 3])
print(np_sigmoid(x))

"""
1.2 create a gradient function
"""
def sigmoid_grad(x):
    s = np_sigmoid(x)
    ds = s * (1-s)
    return ds
x = np.array([1, 2, 3])
print(sigmoid_grad(x))

"""
1.3 reshape array
"""
# np.shape use to get dimensions
# np.reshape use to rebuild the dimensions
def image2vector(image):
    v = image.reshape((image.shape[0]*image.shape[1]* image.shape[2], 1))
    print(image.shape)
    print(v.shape)
    return v
image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])
print(image2vector(image))

"""
1.4 Line of standardized
"""
def normalizateRows(x):
    x_norm = np.linalg.norm(x,axis=1,keepdims=True)
    x = x/x_norm
    return x
x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print(normalizateRows(x))

"""
1.5 Broadcasting and softmax function
"""
def softmax(x):
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp,axis=1,keepdims=True)
    s = x_exp/x_sum
    return s
x = np.array([
    [9, 2, 5, 0, 0],
    [7, 5, 0, 0 ,0]])
print(softmax(x))

"""
2.0 Vectorization
"""
import time
x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]
# -----------------------Classic--------------------
# CLASSIC DOT PRODUCT OF VECTORS IMPLEMENTATION
tic = time.process_time()
dot = 0
for i in range(len(x1)):
    dot += x1[i]*x2[i]
toc = time.process_time()
print("dot = " + str(dot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

# CLASSIC OUTER PRODUCT IMPLEMENTATION
tic = time.process_time()
outer = np.zeros((len(x1),len(x2))) # we create a len(x1)*len(x2) matrix with only zeros
for i in range(len(x1)):
    for j in range(len(x2)):
        outer[i,j] = x1[i]*x2[j]
toc = time.process_time()
print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

# CLASSIC ELEMENTWISE IMPLEMENTATION
tic = time.process_time()
mul = np.zeros(len(x1))
for i in range(len(x1)):
    mul[i] = x1[i]*x2[i]
toc = time.process_time()
print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

# CLASSIC GENERAL DOT PRODUCT IMPLEMENTATION
W = np.random.rand(3,len(x1)) # Random 3*len(x1) numpy array
tic = time.process_time()
gdot = np.zeros(W.shape[0])
for i in range(W.shape[0]):
    for j in range(len(x1)):
        gdot[i] += W[i,j]*x1[j]
toc = time.process_time()
print ("gdot = " + str(gdot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

# ---------------------Vectorization-----------------
x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

### VECTORIZED DOT PRODUCT OF VECTORS ###
tic = time.process_time()
dot = np.dot(x1,x2)
toc = time.process_time()
print ("dot = " + str(dot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED OUTER PRODUCT ###
tic = time.process_time()
outer = np.outer(x1,x2)
toc = time.process_time()
print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED ELEMENTWISE MULTIPLICATION ###
tic = time.process_time()
mul = np.multiply(x1,x2)
toc = time.process_time()
print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED GENERAL DOT PRODUCT ###
tic = time.process_time()
dot = np.dot(W,x1)
toc = time.process_time()
print ("gdot = " + str(dot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

"""
2.1 implement the lost function of L1&L2
"""
def L1(yhat, y):
    loss = np.sum(np.abs(y-yhat))
    return loss

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat,y)))

def L2(yhat, y):
    loss = np.dot((y - yhat),(y - yhat).T)
    return loss

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))