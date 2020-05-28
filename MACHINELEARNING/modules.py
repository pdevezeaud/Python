# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:42:32 2020

@author: Philippe
"""

# module important pour la data science

import math
import random
import statistics
import os
import glob

########################################
#  MATH
#######################################

x= math.pi
statistics.variance()
random.choice()
random.seed()
random.randint()
print(random.sample(range(100),10))

random.shuffle()

print(os.getcwd())

filenames = glob.glob("*.txt")

for file in filenames:
    with open(file,'r') as f:
        print(f.read())
        f.close()
