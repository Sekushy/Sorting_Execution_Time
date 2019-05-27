#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import csv

# In next cell
df = pd.read_csv('Execution_times.csv')
saved_column = df.column[0]
plt.figure(1)
plt.plot(saved_column, 'b*-', label="Merge Sort")
plt.show()