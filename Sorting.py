#!/usr/bin/env python
import time

# Computation Complexity O(n^2) - Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        

# Computation Complexity O(n) - Insertion Sort
def insertionSort(arr):
    for index in range(1, len(arr)):
        current = arr[index]
        position = index

        while position > 0 and arr[position-1] > current:
            arr[position] = arr[position-1]
            position -= 1

        arr[position] = current

# Computation Complexity O(n) - Merge Sort
def mergeSort(arr):
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 

        
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 

        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1