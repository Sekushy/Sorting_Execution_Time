#!/usr/bin/env python
import time
from random import randint
import csv
import Sorting

def runSortingAlgorithm(sortingAlgorithmName):
    # Create a temporary array that takes on the value of the randomized array each time so that the execution times remain constant
    temporaryArray = randomizedArray
    print('------Begin ' + sortingAlgorithmName + '------')
    execution = 'Sorting.{}(temporaryArray)'.format((sortingAlgorithmName[0].lower() + sortingAlgorithmName[1:]).replace(' ', ''))
    startExecutionTime = time.time()
    exec(execution)
    finalExecutionTime = float('{0:.4f}'.format(time.time() - startExecutionTime))
    print('Exection time in seconds: {}'.format(finalExecutionTime, end='\n'))
    sortingColumn = '{}'.format((sortingAlgorithmName[0].lower() + sortingAlgorithmName[1:]).replace(' ', '') + 'Column.append(' + str(finalExecutionTime) + ')')
    exec(sortingColumn)

if __name__ == '__main__':
    sizeOfArray = int(input('Please input the size of your array: '))

    # Code that generates the random array of numbers depending on the size
    # given by the user
    randomizedArray = []

    for i in range(sizeOfArray):
        randomizedArray.append(randint(0, 10))
    
    bubbleSortColumn = []
    mergeSortColumn = []
    insertionSortColumn = []

    columnNames = ['Bubble Sort', 'Merge Sort', 'Insertion Sort']

    for i in range(9):
        j = i % len(columnNames)
        runSortingAlgorithm(str(columnNames[j]))
        i = i + 1

with open('startExecutionTimes_' + str(sizeOfArray) + '.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(columnNames)
    writer.writerows(zip(bubbleSortColumn, mergeSortColumn, insertionSortColumn))