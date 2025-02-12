#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:29:16 2025

@author: liamthompson
"""
import numpy as np 

A = 2.53e11
B = 5.42e3

t_prime_0 = 289.15

a = -(100000*1005) / (2466*0.622*1000)
b = 22.391*100 + ((100000*1005*289.15) / (2466 * 1000 * 0.622))

def t_prime_e_prime_finder(t_prime):
    t_prime = B / (np.log(A / (a*t_prime+b)))
    return t_prime

converge = 1e-100
iteration = 0
difference = float("inf")

while difference >= converge:
    iteration +=1
    t_prime = t_prime_e_prime_finder(t_prime_0)
    difference = abs(t_prime - t_prime_0)
    t_prime_0 = t_prime
    
    print(f"Iteration {iteration}: T' = {t_prime_0:.3f} K, Difference = {difference:.3f} K")

print(f"Final T'': {t_prime_0:.2f} K")

