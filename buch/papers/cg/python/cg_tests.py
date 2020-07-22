# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:59:57 2020

@author: runterer
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import sklearn.datasets
import time


class CG:
    def __init__(self):
        self.__reset()
        
    def __reset(self):
        self.d = None
        self.r = None
        
        
    def descent_step(self, A, b, x):
        if self.r is None:
            self.r = b - np.dot(A, x)
        if self.d is None:
            self.d = self.r
        
        denominator = np.dot(self.d.T, np.dot(A, self.d))
        
        alpha = np.dot(self.d.T, self.r) / denominator
        x_new = x + self.d*alpha
        
        self.r = b - np.dot(A, x_new)
        
        self.d = self.r - self.d * np.dot(self.d.T, np.dot(A, self.r)) / denominator
        return x_new
    
def create_sym_pos_def_matrix(n=10, rand_factor=10, rand_seed=0):
    np.random.seed(rand_seed)
    # A = sklearn.datasets.make_spd_matrix(n, random_state=rand_seed)*rand_factor
    A = np.random.randn(n,n)
    A = A.T*A
    # A = A + n*np.eye(n,n)
    # A = A*rand_factor
    
    b = np.random.rand(n)*rand_factor
    x0 = np.random.rand(n)*rand_factor
    return A, b, x0

if __name__ == "__main__":
    n = 1000
    A, b, x0 = create_sym_pos_def_matrix(n=n)
    print("Konditionierungszahl von A: {}".format(np.linalg.cond(A)))
    cg = CG()
    residuals = []
    times = []
    x = cg.descent_step(A,b,x0)
    residuals.append(np.linalg.norm(cg.r,2))
    for i in range(1,n):
        if i % 100 == 0:
            print("step {} of {}".format(i, n))
        t = time.time()
        x = cg.descent_step(A,b,x)
        times.append(time.time()-t)
        residuals.append(np.linalg.norm(cg.r,2))
    plt.plot(residuals)
    plt.yscale("log")
    print("time for one step: {}".format(np.mean(times)))
    print("total time for perfect solve: {}".format(np.mean(times)*n))
    
    t = time.time()
    x2 = np.dot(np.linalg.inv(A), b)
    t = time.time()-t
    print("total time for inversion: {}".format(t))
    
    
    
    