
## https://stackoverflow.com/questions/35572000/how-can-i-plot-a-confusion-matrix
## https://seaborn.pydata.org/generated/seaborn.heatmap.html

import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
array = [
            [500,0,0,0,0,0,0,0,39,0,3,0,1,1,0,7],# A
            [3,432,48,0,0,0,0,0,0,0,0,0,0,0,0,0],# B
            [1,	121,513,0,0,0,0,0,0,0,0,0,1,0,0,0], # C
            [1,0,0,522,31,0,0,0,0,0,2,0,0,0,0,34],# D
            [0,0,0,33,532,0,0,0,0,0,1,0,0,0,0,17], # E
            [0,0,0,0,1,	5,0,0,0,0,0,0,0,0,0,0], # F
            [3,3,2,0,0,0,559,0,0,0,2,0,0,0,0,0],# G
            [0,0,0,0,0,0,0,501,7,0,0,0,0,0,0,0],# H
            [1,0,0,0,0,0,0,0,1918,0,0,0,0,0,0,1],# I
            [1,0,0,0,0,0,0,0,1,37,0,0,0,0,0,0], # J
            [10,0,0,1,0,0,1,0,0,0,358,6,0,1,0,46],# K
            [18,0,0,0,0,0,0,0,0,0,6,578,0,0,0,2],# L
            [1,0,0,0,0,0,0,5,0,0,0,0,1063,0,1,0],# M
            [3,0,0,	0,0,0,0,0,0,0,2,0,0,188,1,0],# N
            [0,0,0,0,0,0,1,0,0,0,0,0,0,2,395,1], # O
            [0,0,0,0,0,	0,0,0,0,0,0,0,0,0,0,165],# P

        ]
df_cm = pd.DataFrame(array, index = [i for i in "ABCDEFGHIJKLMNOP"],
                  columns = [i for i in "ABCDEFGHIJKLMNOP"])
plt.figure(figsize = (13,10))
sn.heatmap(df_cm, annot=True, fmt="d", linewidths=.5, cmap=sn.mpl_palette("Set3_r", 20))
plt.savefig("output.svg")


