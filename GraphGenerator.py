#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import csv

def readDataFromCsv(position_y, nameOfFile):
    exampleFile = open(nameOfFile)
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    print(exampleData)

    tempList = list()
    for i in range(len(exampleData)):
        if i != 0:
            tempList.append(exampleData[i][position_y])  
    return tempList

def getColumnHeaderAt(position, nameOfFile):
    with open(nameOfFile, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
    return row1[position]

def generateGraph(nameOfFile):
    plt.figure()

    bubbleSortData = readDataFromCsv(0, nameOfFile)
    mergeSortData = readDataFromCsv(1, nameOfFile)
    insertionSortData = readDataFromCsv(2, nameOfFile)

    # Populate and customize sub-plot 1
    plt.subplot(3, 1, 1)
    plt.plot(bubbleSortData, range(len(bubbleSortData)), 'b*-')
    plt.title(getColumnHeaderAt(0, nameOfFile))
    plt.ylabel('Iteration number')
    plt.xlabel('Execution time')

    # Populate and customize sub-plot 1
    plt.subplot(3, 1, 2)
    plt.plot(mergeSortData, range(len(bubbleSortData)), 'g:+')
    plt.title(getColumnHeaderAt(1, nameOfFile))


    # Populate and customize sub-plot 1
    plt.subplot(3, 1, 3)
    plt.plot(insertionSortData, range(len(bubbleSortData)),'r*-')
    plt.title(getColumnHeaderAt(2, nameOfFile))

    plt.tight_layout()
    plt.show()

