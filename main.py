#!/usr/bin/env python
import time, datetime
from random import randint
import csv
import Sorting
import GraphGenerator

def generateRandomArray(sizeOfArray):
    randomizedArray = []
    for i in range(sizeOfArray):
        randomizedArray.append(randint(0, 10))
    return randomizedArray

def printExectionTime(sortingAlgorithmName, executionTime):
     print('------Begin ' + sortingAlgorithmName + '------')
     print('Exection time in seconds: {}'.format(executionTime, end='\n'))

def runSortingAlgorithm(sortingAlgorithmName, temporaryArray):
    # Assign a temporary array that takes on the value of the randomized array each time so that the execution times remain constant
    executeSorting = 'Sorting.{}(temporaryArray)'.format((sortingAlgorithmName[0].lower() + sortingAlgorithmName[1:]).replace(' ', ''))
    startExecutionTime = time.time()
    exec(executeSorting)
    finalExecutionTime = float('{0:.2f}'.format(time.time() - startExecutionTime))
    printExectionTime(sortingAlgorithmName, finalExecutionTime)
    sortingColumn = '{}'.format((sortingAlgorithmName[0].lower() + sortingAlgorithmName[1:]).replace(' ', '') + 'Column.append(' + str(finalExecutionTime) + ')')
    exec(sortingColumn)


if __name__ == '__main__':
    sizeOfArray = int(input('Please input the size of your array: '))

    columnNames = ['Bubble Sort', 'Merge Sort', 'Insertion Sort']
    bubbleSortColumn = []
    mergeSortColumn = []
    insertionSortColumn = []

    for i in range(len(columnNames) * len(columnNames)):
        j = i % len(columnNames)
        runSortingAlgorithm(str(columnNames[j]),generateRandomArray(sizeOfArray))
        i = i + 1
    
    with open('startExecutionTimes_' + str(sizeOfArray) + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(columnNames)
        writer.writerows(zip(bubbleSortColumn, mergeSortColumn, insertionSortColumn))

    GraphGenerator.generateGraph('startExecutionTimes_' + str(sizeOfArray) + '.csv')