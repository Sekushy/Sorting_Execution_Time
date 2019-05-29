#!/usr/bin/env python
import matplotlib.pyplot as plt
import csv

# In next cell
exampleFile = open('startExecutionTimes_10000.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
