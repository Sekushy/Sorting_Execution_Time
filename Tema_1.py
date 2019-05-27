#!/usr/bin/env python
import time
from random import randint
import csv

import Sorting

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

    for i in range(3):
        # Create a temporary array that takes on the value of the randomized array so that the execution times remain constant
        temporaryArray = randomizedArray

        # Merge Algorithm
        print('------Begin merge sort------')
        execution_time = time.time()
        Sorting.mergeSort(temporaryArray)
        print('Exection time in seconds: %s' % (time.time() - execution_time))
        mergeSortColumn.append(round(time.time() - execution_time))

        # Insertion Algorithm
        print('------Begin insertion sort------')
        execution_time = time.time()
        Sorting.insertionSort(temporaryArray)
        print('Exection time in seconds: %s' % (time.time() - execution_time))
        insertionSortColumn.append(time.time() - execution_time)        
        
        # Bubble Algorithm
        print('------Begin bubble sort------')
        execution_time = time.time()
        Sorting.bubbleSort(temporaryArray)
        print('Exection time in seconds: %s\n' % (time.time() - execution_time))
        bubbleSortColumn.append(time.time() - execution_time)
        
        i = i + 1

with open('Execution_times.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(zip(bubbleSortColumn, mergeSortColumn, insertionSortColumn))