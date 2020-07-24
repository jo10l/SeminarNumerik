#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 08:50:37 2020

@author: terminator
"""

import numpy as np

# def rk(x_vec, func_deriv, y0, h):#first attempt, worked
#     y=[]
#     y.append(y0)
#     for i in range(len(x_vec)-1):
#         k1=func_deriv(x[i], y[i])
#         k2=func_deriv(x[i]+h/2, y[i]+h*k1/2)
#         k3=func_deriv(x[i]+h/2, y[i]+h*k2/2)
#         k4=func_deriv(x[i]+h, y[i]+h*k3)
#         y.append(y[i]+h/6*(k1+2*k2+2*k3+k4))
#     return y

    
def rk_fs(x0, y0, x_end, deriv, h, x_start=None, debug=False):
    """runge-kutta fixed step size: x0, y0, x_end, deriv_function(x,y), step-size [, x_start]"""
    x=[x0]
    y=[y0]
    if debug:
        k=[(0,0,0,0,0)]
    while(x[-1]<x_end):
        k1=deriv(x[-1], y[-1])
        k2=deriv(x[-1]+h/2, y[-1]+h*k1/2)
        k3=deriv(x[-1]+h/2, y[-1]+h*k2/2)
        k4=deriv(x[-1]+h, y[-1]+h*k3)
        
        x.append(x[-1]+h)
        y.append(y[-1]+h/6*(k1+2*k2+2*k3+k4))
        if debug:
            k.append((h, k1, k2, k3, k4))
        
    if x_start is not None:
        while(x[0]>x_start):
            k1=deriv(x[0], y[0])
            k2=deriv(x[0]-h/2, y[0]-h*k1/2)
            k3=deriv(x[0]-h/2, y[0]-h*k2/2)
            k4=deriv(x[0]-h, y[0]-h*k3)
            
            x.insert(0, x[0]-h)
            y.insert(0, y[0]-h/6*(k1+2*k2+2*k3+k4))
            if debug:
                k.insert(0, (h, k1, k2, k3, k4))
        
    if debug:
        return x, y, k
    
    
    else:
        return x, y   
    
def rk_system(x0, g_vec, x_end, deriv, h):
    '''runge-kutta for DGL order 2+ (x0, start_vector, x_end, func(x, y) for y^n, step size'''
    size=len(g_vec)
    x=[x0]
    y=[np.array(g_vec)]
    matrix=np.zeros((size,size))
    matrix[:-1, 1:]=np.eye(size-1)
    vector_deriv_function=np.zeros(size)
    vector_deriv_function[-1]=1 #[0, 0, ..., 0, 1]
    while(x[-1]<x_end):
        y_ss=y[-1]  #y_step_start
        x_ss=x[-1]  #x_step_start
        k1=matrix @ y_ss+deriv(x_ss, y_ss)*vector_deriv_function
        y_k1=y_ss+h/2*k1#y-vector for calculating k2 (calculated with k1)
        k2=matrix @ y_k1+deriv(x_ss+h/2, y_k1)*vector_deriv_function
        y_k2=y_ss+h/2*k2#y-vector for calculating k3 (calculated with k2)
        k3=matrix @ y_k2+deriv(x_ss+h/2, y_k2)*vector_deriv_function
        y_k3=y_ss+h*k3#y-vector for calculating k4 (calculated with k3)
        k4=matrix @ y_k3+deriv(x_ss+h, y_k3)*vector_deriv_function
        
        x.append(x[-1]+h)
        y.append(y_ss+h/6*(k1+2*k2+2*k3+k4))
        #y.append(y_ss+h*k1)    #euler
    return x, y

def rk_system_nd(x0, g_vec, x_end, deriv, h):
    '''runge_kutta n-dimensional m'th degreee (x0, [np.array([y1(0), y2(0)]),np.array([y1'(0), y2'(0)]), ...], x_end, deriv_function(x, y), step_size)'''     
    size=len(g_vec) #degree of dgl
    dimensions=len(g_vec[0])
    x=[x0]
    y=[np.array(g_vec)]
    matrix=np.zeros((size,size))
    matrix[:-1, 1:]=np.eye(size-1)
    vector_deriv_function=np.zeros(size)
    vector_deriv_function[-1]=1 #[0, 0, ..., 0, 1]
    while(x[-1]<x_end):
        
        y_ss=y[-1]  #y_step_start
        x_ss=x[-1]  #x_step_start

        k1=matrix @ y_ss + np.array([i*deriv(x_ss, y_ss) for i in vector_deriv_function])
        y_k1=y_ss+h/2*k1#y-vector for calculating k2 (calculated with k1)
        
        k2=matrix @ y_k1+np.array([i*deriv(x_ss+h/2, y_k1) for i in vector_deriv_function])
        y_k2=y_ss+h/2*k2#y-vector for calculating k3 (calculated with k2)
         
        k3=matrix @ y_k2+np.array([i*deriv(x_ss+h/2, y_k2)for i in vector_deriv_function])
        y_k3=y_ss+h*k3#y-vector for calculating k4 (calculated with k3)
            
        k4=matrix @ y_k3+np.array([i*deriv(x_ss+h, y_k3) for i in vector_deriv_function])
            
        x.append(x[-1]+h)
        y.append(y_ss+h/6*(k1+2*k2+2*k3+k4))
        #y.append(y_ss+h*k1)    #euler
    return x, y
        
def rk_system_nd_ssc_single_test_step(x0, g_vec, x_end, deriv, hmin, hmax, qfactor):
    '''runge_kutta n-dimensional m'th degreee (x0, [np.array([y1(0), y2(0)]),np.array([y1'(0), y2'(0)]), ...], x_end, deriv_function(x, y), step_size_min, step_size_max, qfactor)'''
    htest=hmax
    size=len(g_vec) #degree of dgl
    dimensions=len(g_vec[0])
    x=[x0]
    y=[np.array(g_vec)]
    matrix=np.zeros((size,size))
    matrix[:-1, 1:]=np.eye(size-1)
    
    while(x[-1]<x_end):
        
        y_ss=y[-1]  #y_step_start
        x_ss=x[-1]  #x_step_start

        k1=matrix @ y_ss +np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss, y_ss)])
        
        y_test=y_ss+htest*k1
        ktest=matrix @ y_test+np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss+htest, y_test)])
        y_difference=np.max(abs(k1[-1]-ktest[-1]))
        h=htest/y_difference/qfactor
        if(h<hmin):
            h=hmin
        elif h>hmax:
            h=hmax
        
        y_k1=y_ss+h/2*k1#y-vector for calculating k2 (calculated with k1)
        
        
        k2=matrix @ y_k1+np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss+h/2, y_k1)])
        y_k2=y_ss+h/2*k2#y-vector for calculating k3 (calculated with k2)
         
        k3=matrix @ y_k2+np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss+h/2, y_k2)])
        y_k3=y_ss+h*k3#y-vector for calculating k4 (calculated with k3)
            
        k4=matrix @ y_k3+np.vstack([np.tile(np.full(dimensions, 0), (size-1, 1)), deriv(x_ss+h, y_k3)])
            
        x.append(x[-1]+h)
        y.append(y_ss+h/6*(k1+2*k2+2*k3+k4))
        #y.append(y_ss+h*k1)    #euler
    return x, y

def rk_system_nd_ssc_fehlberg(x0, g_vec, x_end, deriv, hmin, hmax, epsilon=0.01, hstart=None):
    '''runge_kutta n-dimensional m'th degreee fehlberg step size control(x0, [np.array([y1(0), y2(0)]),np.array([y1'(0), y2'(0)]), ...], x_end, deriv_function(x, y), step_size_min, step_size max, local_error, hstart)
    
    uses 4 steps forth order rk combined with 6 steps fifth order rk'''
    if hstart:
        h=hstart
    else:
        h=hmin
    size=len(g_vec) #degree of dgl
    dimensions=len(g_vec[0])
    x=[x0]
    y=[np.array(g_vec)]
    matrix=np.zeros((size,size))
    matrix[:-1, 1:]=np.eye(size-1)
    vector_deriv_function=np.full(dimensions, 0)
    while(x[-1]<x_end):
        step_ok=False
        while(not step_ok):
            y_ss=y[-1]  #y_step_start
            x_ss=x[-1]  #x_step_start
    
            k1=matrix @ y_ss +np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss, y_ss)])
            hk1=h*k1#y-vector for calculating k2 (calculated with k1)
            
            y2=y_ss+2/9*hk1        
            k2=matrix @ y2+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+2/9*h, y2)])
            hk2=h*k2#y-vector for calculating k3 (calculated with k2)
            
            y3=y_ss+1/12*hk1+1/4*hk2
            k3=matrix @ y3+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+1/3*h, y3)])
            hk3=h*k3
            
            y4=y_ss+69/128*hk1-243/128*hk2+135/64*hk3
            k4=matrix @ y4+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+3/4*h, y4)])
            hk4=h*k4
            
            y5=y_ss-17/12*hk1+27/4*hk2-27/5*hk3+16/15*hk4
            k5=matrix @ y5+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+h, y5)])
            hk5=h*k5
            
            y6=y_ss+65/432*hk1-5/16*hk2+13/16*hk3+4/27*hk4+5/144*hk5
            k6=matrix @ y6+np.vstack([np.tile(vector_deriv_function, (size-1, 1)), deriv(x_ss+5/6*h, y6)])
            hk6=h*k6
            
            y_4th=y_ss+1/9*hk1+9/20*hk3+16/45*hk4+1/12*hk5
            #y_5th=y_ss+47/450*hk1+12/25*hk3+32/225*hk4+1/30*hk5+6/25*hk6
            T=np.max(abs((-2*hk1+9*hk3-64*hk4-15*hk5+72*hk6)/300))
            
            if(T<epsilon/20):       #very accurate, increase step size
                x.append(x_ss+h)
                y.append(y_4th)
                h=2*h
                
                if(h>hmax):
                    h=hmax
                
                step_ok=True
            elif(T>epsilon):    #unaccurate, decrease step size, repeat step
                if(h==hmin):        #already minimum step size
                    x.append(x_ss+h)
                    y.append(y_4th)
                    step_ok=True
                else:
                    h=h/2
                    #step_ok=False
                    if(h<hmin):
                        h=hmin
                
            else:           #accurate enough, keep step size
                x.append(x_ss+h)
                y.append(y_4th)
                step_ok=True
    return x, y