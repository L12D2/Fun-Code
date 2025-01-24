#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:23:22 2024

@author: liamthompson
"""

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

path = [
    "/Users/liamthompson/Desktop/metr2613 data/NWC0_05F.dat",
    "/Users/liamthompson/Desktop/metr2613 data/NWC1_05F.dat",
    "/Users/liamthompson/Desktop/metr2613 data/NWC2_05F.dat",
    "/Users/liamthompson/Desktop/metr2613 data/NWC3_05F.dat",
    "/Users/liamthompson/Desktop/metr2613 data/NWC4_05F.dat",
    "/Users/liamthompson/Desktop/metr2613 data/NWC5_05F.dat",
    "/Users/liamthompson/Desktop/metr2613 data/NWC6_05F.dat",
    "/Users/liamthompson/Desktop/metr2613 data/NWC7_05F.dat"
    #"/Users/liamthompson/Desktop/metr2613 data/NWC8_05F.dat"
    ]

#%% 

fig1, ax1 = plt.subplots(figsize=(20,10), dpi = 600)
fig2, ax2 =plt.subplots(figsize=(6,3), dpi = 600)
eight = pd.read_csv("/Users/liamthompson/Desktop/metr2613 data/NWC8_05F.dat", skiprows = [0,2,3]) #(Ptemp???)

# Define a list of colors for the plots
colors = ["b", "c", "g", "k", "m", "r", "y", "purple"]
#line_styles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
#markers = ['o', 's', '^', 'D', '*', 'x', '+', 'h']


# Loop through the file paths and read each file
for i, file_path in enumerate(path):
    df = pd.read_csv(file_path, skiprows=[0,2,3])
    
    # Convert the TIMESTAMP column to datetime
    df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"], errors="coerce")
    
    # Plot the data
    ax1.plot(df["TIMESTAMP"], df["TAIR"], label=f'NWC{i}', color=colors[i], lw = 1.05)
    #ax1.plot(eight["TIMESTAMP"], eight["PTemp"],label = "NWC08")
    sns.kdeplot(data = df["TAIR"], ax = ax2, label=f'NWC{i}', color=colors[i], lw = 1.05)
    #sns.kdeplot(eight["PTemp"], ax = ax2, label = "NWC08")
    #ax2.hist(df["TAIR"], bins = 50, label = f"File {i}", color = colors[i])

eight["TIMESTAMP"] = pd.to_datetime(eight["TIMESTAMP"], errors = "coerce")
ax1.plot(eight["TIMESTAMP"], eight["PTemp"], label = "NWC8", color = "orange")
sns.kdeplot(eight["PTemp"], ax = ax2, label = "NWC8", color = "orange")


ax1.set_xlabel("Time")
ax1.set_ylabel("Temp (C)")
ax1.legend()
ax1.set_title("Time Series")

ax2.set_xlabel("Temp")
ax2.set_ylabel("Freq")
ax2.legend()
ax2.set_title("Frequency")


# Show the plot
plt.show()

#%% 
# tair, srad, relh, wspd
fig, ax = plt.subplots(5, 3, figsize=(36, 24))
colors = ["b", "c", "g", "k", "m", "r", "y", "purple"]
eight = pd.read_csv("/Users/liamthompson/Desktop/metr2613 data/NWC8_05F.dat", skiprows = [0,2,3]) #(Ptemp???)


for i, file_path in enumerate(path):
    df = pd.read_csv(file_path, skiprows=[0,2,3])
    
    # Convert the TIMESTAMP column to datetime
    df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"], errors="coerce")

    ax[0,0].plot(df["TIMESTAMP"], df["TAIR"], label=f'NWC{i}', color=colors[i], lw = 1.05)
    ax[0,0].set_title("Timseries")
    ax[0,0].set_ylabel("Temp (C)")
    ax[0,0].set_xlabel("Time")
    sns.kdeplot(data = df["TAIR"], ax = ax[0,1], label=f'NWC{i}', color=colors[i], lw = 1.05)
    ax[0,1].set_title("Temp Distribution")
    ax[0,1].set_xlabel("Temp (C)")
    box = ax[0, 2].boxplot(df["TAIR"], positions=[i], widths=0.8)  
    ax[0,2].set_ylabel("Temp (C)")
    ax[0,2].set_xlabel("Station")
    ax[0,2].set_title("Boxplot of Station")
    for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box[element], color=colors[i])
    
    ax[1, 0].plot(df["TIMESTAMP"], df["RELH"], label=f'NWC{i}', color=colors[i], lw=1.05)
    ax[1, 0].set_title("Relative Humidity Time Series")
    ax[1, 0].set_ylabel("Relative Humidity (%)")
    ax[1, 0].set_xlabel("Time")
    
    sns.kdeplot(data=df["RELH"], ax=ax[1, 1], label=f'NWC{i}', color=colors[i], lw=1.05)
    ax[1, 1].set_title("Relative Humidity Distribution")
    ax[1, 1].set_ylabel("Density")
    ax[1, 1].set_xlabel("Relative Humidity (%)")
    
    box = ax[1, 2].boxplot(df["RELH"], positions=[i], widths=0.8)  
    ax[1, 2].set_ylabel("Relative Humidity (%)")
    ax[1, 2].set_xlabel("Station")
    ax[1, 2].set_title("Boxplot of Relative Humidity")
    for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box[element], color=colors[i])
    
    ax[2, 0].plot(df["TIMESTAMP"], df["WSPD"], label=f'NWC{i}', color=colors[i], lw=1.05)
    ax[2, 0].set_title("WSPD Time Series")
    ax[2, 0].set_ylabel("WSPD (m/s)")
    ax[2, 0].set_xlabel("Time")
    
    sns.kdeplot(data=df["WSPD"], ax=ax[2, 1], label=f'NWC{i}', color=colors[i], lw=1.05)
    ax[2, 1].set_title("WSPD Distribution")
    ax[2, 1].set_ylabel("Density")
    ax[2, 1].set_xlabel("WSPD (m/s)")
    
    box = ax[2, 2].boxplot(df["WSPD"], positions=[i], widths=0.8)  
    ax[2, 2].set_ylabel("WSPD (m/s)")
    ax[2, 2].set_xlabel("Station")
    ax[2, 2].set_title("Boxplot of WSPD")
    for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box[element], color=colors[i])
        
    ax[3, 0].plot(df["TIMESTAMP"], df["BATV"], label=f'NWC{i}', color=colors[i], lw=1.05)
    ax[3, 0].set_title("BATV Time Series")
    ax[3, 0].set_ylabel("BATV (V)")
    ax[3, 0].set_xlabel("Time")
    
    sns.kdeplot(data=df["BATV"], ax=ax[3, 1], label=f'NWC{i}', color=colors[i], lw=1.05)
    ax[3, 1].set_title("BATV Distribution")
    ax[3, 1].set_ylabel("Density")
    ax[3, 1].set_xlabel("BATV (V)")
    
    box = ax[3, 2].boxplot(df["BATV"], positions=[i], widths=0.8)  
    ax[3, 2].set_ylabel("BATV (V)")
    ax[3, 2].set_xlabel("Station")
    ax[3, 2].set_title("Boxplot of BATV")
    for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box[element], color=colors[i])
        
    # Convert SRAD to numeric
    df["SRAD"] = pd.to_numeric(df["SRAD"], errors="coerce")
    # Replace NaN values with 0
    df["SRAD"].fillna(0, inplace=True)

    ax[4, 0].plot(df["TIMESTAMP"], df["SRAD"], label=f'NWC{i}', color=colors[i], lw=1.05)
    ax[4, 0].set_title("Solar Radiation Time Series")
    ax[4, 0].set_ylabel("Solar Radiation (w/m^2)")
    ax[4, 0].set_xlabel("Time")

    sns.kdeplot(data=df["SRAD"], ax=ax[4, 1], label=f'NWC{i}', color=colors[i], lw=1.05)
    ax[4, 1].set_title("Solar Radiation Distribution")
    ax[4, 1].set_ylabel("Density")
    ax[4, 1].set_xlabel("Solar Radiation (w/m^2)")
    
    box = ax[4, 2].boxplot(df["SRAD"], positions=[i], widths=0.8)  
    ax[4, 2].set_ylabel("Solar Radiation (w/m^2)")
    ax[4, 2].set_xlabel("Station")
    ax[4, 2].set_title("Boxplot of Solar Radiation")
    for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box[element], color=colors[i])



eight["TIMESTAMP"] = pd.to_datetime(eight["TIMESTAMP"], errors = "coerce")
ax[0,0].plot(eight["TIMESTAMP"], eight["PTemp"], label = "NWC8", color = "orange")
sns.kdeplot(eight["PTemp"], ax = ax[0,1], label = "NWC8", color = "orange")
box = ax[0, 2].boxplot(eight["PTemp"], positions=[len(path)], widths=0.8)
for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
    plt.setp(box[element], color="orange")
    
eight["TIMESTAMP"] = pd.to_datetime(eight["TIMESTAMP"], errors = "coerce")
ax[1,0].plot(eight["TIMESTAMP"], eight["RELH"], label = "NWC8", color = "orange")
sns.kdeplot(eight["RELH"], ax = ax[1, 1], label = "NWC8", color = "orange")
box = ax[1, 2].boxplot(eight["RELH"], positions=[len(path)], widths=0.8)
for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
    plt.setp(box[element], color="orange")
    
eight["TIMESTAMP"] = pd.to_datetime(eight["TIMESTAMP"], errors = "coerce")
ax[2,0].plot(eight["TIMESTAMP"], eight["WSPD"], label = "NWC8", color = "orange")
sns.kdeplot(eight["WSPD"], ax = ax[2,1], label = "NWC8", color = "orange")
box = ax[2, 2].boxplot(eight["WSPD"], positions=[len(path)], widths=0.8)
for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
    plt.setp(box[element], color="orange")

eight["TIMESTAMP"] = pd.to_datetime(eight["TIMESTAMP"], errors = "coerce")
ax[3,0].plot(eight["TIMESTAMP"], eight["Batt_volt_Min"], label = "NWC8", color = "orange")
sns.kdeplot(eight["Batt_volt_Min"], ax = ax[3,1], label = "NWC8", color = "orange")
box = ax[3, 2].boxplot(eight["Batt_volt_Min"], positions=[len(path)], widths=0.8)
for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
    plt.setp(box[element], color="orange")


eight["SRAD"] = pd.to_numeric(eight["SRAD"], errors="coerce")
# Replace NaN values with 0
eight["SRAD"].fillna(0, inplace=True)

eight["TIMESTAMP"] = pd.to_datetime(eight["TIMESTAMP"], errors = "coerce")
ax[4,0].plot(eight["TIMESTAMP"], eight["SRAD"], label = "NWC8", color = "orange")
sns.kdeplot(eight["SRAD"], ax = ax[4,1], label = "NWC8", color = "orange")
box = ax[4, 2].boxplot(eight["SRAD"], positions=[len(path)], widths=0.8)
for element in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
    plt.setp(box[element], color="orange")

plt.subplots_adjust(top=1.1)
plt.suptitle("SP2024 Station Data")
plt.tight_layout()
plt.savefig("SP2024.png")
plt.show()

