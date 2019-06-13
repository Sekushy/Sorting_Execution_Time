#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import csv

def readDataFromCsv(position_y, nameOfFile):
    exampleFile = open(nameOfFile)
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)

    tempList = list()
    for i in range(len(exampleData)):
        if i != 0:
            tempList.append(exampleData[i][position_y])
    tempList = [float(i) for i in tempList]  
    return tempList

def getColumnHeaderAt(position, nameOfFile):
    with open(nameOfFile, newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        firstRow = next(csvReader)
    return firstRow[position]

def generateGraph(nameOfFile):
    plt.figure()

    bubbleSortData = readDataFromCsv(0, nameOfFile)
    mergeSortData = readDataFromCsv(1, nameOfFile)
    insertionSortData = readDataFromCsv(2, nameOfFile)

    print(bubbleSortData)
    print(type(bubbleSortData))

    # Populate and customize sub-plot 1
    plt.subplot(3, 1, 1)
    plt.plot(range(len(bubbleSortData)), bubbleSortData, 'b*-')
    plt.title(getColumnHeaderAt(0, nameOfFile))
    plt.xlabel('Iteration number')
    plt.ylabel('Execution time')

        # Populate and customize sub-plot 1
    plt.subplot(3, 1, 2)
    plt.plot(range(len(bubbleSortData)), mergeSortData, 'g:+')
    plt.title(getColumnHeaderAt(1, nameOfFile))
    plt.xlabel('Iteration number')
    plt.ylabel('Execution time')


    # Populate and customize sub-plot 1
    plt.subplot(3, 1, 3)
    plt.plot(range(len(insertionSortData)), insertionSortData,'r*-')
    plt.title(getColumnHeaderAt(2, nameOfFile))
    plt.xlabel('Iteration number')
    plt.ylabel('Execution time')

    plt.tight_layout()
    plt.show()