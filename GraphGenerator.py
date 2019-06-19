#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from random import randint
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

def getRandomLineColor():
    randomLines = ['b', 'g', 'r', 'm', 'c', 'k', 'y']
    return randomLines[randint(0, len(randomLines))]

def generateGraphs(index, totalNumber, sortingData, nameOfFile):
    plt.subplot(totalNumber, 1, (index + 1))
    plt.plot(range(len(sortingData)), sortingData, getRandomLineColor() + '*-')
    plt.title(getColumnHeaderAt(index, nameOfFile))
    plt.xlabel('Iteration number')
    plt.ylabel('Execution time')

def generateGraph(nameOfFile):
    plt.figure()

    bubbleSortData = readDataFromCsv(0, nameOfFile)
    mergeSortData = readDataFromCsv(1, nameOfFile)
    insertionSortData = readDataFromCsv(2, nameOfFile)

    dataList = [bubbleSortData, mergeSortData, insertionSortData]

    for i in range(len(dataList)):
        generateGraphs(i, 3, dataList[i] , nameOfFile)

    plt.tight_layout()
    plt.savefig('Plot_' + nameOfFile + '.png', dpi=600, format='png')
    plt.show()