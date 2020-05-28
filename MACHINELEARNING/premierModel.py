# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:06:43 2020

@author: Philippe
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

house_data = pd.read_csv('house.csv')
house_data = house_data[house_data['loyer'] < 10000]
print(house_data[:10])
plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize=4)
plt.show()
