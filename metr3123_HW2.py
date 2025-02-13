#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:22:18 2025

@author: liamthompson
"""
import numpy as np
import matplotlib.pyplot as plt

p1 = 100000 
Rd = 287 
T = 298.15

velocity_mph = np.arange(0,250) # 210 mph is the START of the EF5 scale, so I upped my upper limit to 250 since there
# have been tornadoes that have had wind speeds up to 300mph. 
velociy_m_per_s = velocity_mph * 5280 * (1/3600) * (1/3.28) 

def cyclostrophic(velociy_m_per_s):
    p0 = (p1*np.exp((-velociy_m_per_s**2) / (2 * Rd * T)))

    return p0 

min_pres = cyclostrophic(velociy_m_per_s)

plt.plot(velociy_m_per_s, min_pres)
plt.xticks(np.arange(0, 115, step=16))

plt.ylabel("Minimum Pressure [Pa]")
plt.xlabel("Wind Speed [m/s]")
plt.title("Minimum Tornado Pressures as a Function of Wind Speed")