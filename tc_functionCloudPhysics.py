#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:11:07 2025

@author: liamthompson
"""
# d) 
import numpy as np

b = 5.42e3
a = 2.53e11
w = 2.138e-3
p0 = 80000
t0 = 268.15
k = 0.286
e = 0.622
tc = 262.5976
td = tc
    
def tc(b, a, e, w, p0, t0, tc, k):
        
    tc_new = b / (np.log(a * e / (w * p0) * (t0 / tc)**(1 / k)))
    return(tc_new)

current_tc = 300

converge = 1e-100
iteration = 0
difference = float("inf")
    
while difference >= converge:
        iteration +=1
        tc_new = tc(b, a, e, w, p0, t0, current_tc, k)
        difference = abs(tc_new - current_tc)
        current_tc = tc_new
    
        print(f"Iteration {iteration}: Tc = {current_tc:.2f} K, Difference = {difference:.2f} K")

print(f"Final Tc: {current_tc:.2f} K")

#%% 
#c)

b = 5.42e3
a = 2.53e11
w = 2.138e-3
p0 = 80000
t0 = 268.15
k = 0.286
e = 0.622
tc = 261.48
l = 2.837e6 # @ T ~= -5C
cp = 1005
tw = tc
    
def tw(b, a, e, w, p0, t0, tc, k, l, cp, current_tw):
    tw_new = t0 - (l / cp)*((e / p0) * a * np.exp((-b / current_tw)) - w)
    return tw_new

current_tw = 300

converge = 1e-100
iteration = 0
difference = float("inf")
    
while difference >= converge:
        iteration +=1
        tw_new = tw(b, a, e, w, p0, t0, tc, k, l, cp, current_tw)
        difference = abs(tw_new - current_tw)
        current_tw = tw_new
    
        print(f"Iteration {iteration}: Tw = {current_tw:.2f} K, Difference = {difference:.2f} K")

print(f"Final Tw: {current_tw:.2f} K")

#%%
from metpy.calc import wet_bulb_potential_temperature

from metpy.units import units

wet_bulb_potential_temperature(800 * units.hPa, -5 * units.degC, -10.5524 * units.degC)




