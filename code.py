#Author of this code: Brent Moran
#We need to import time in order to time how long each function takes to complete.
#We are also importing random to use random integers in our lists. 
#We had to import sys to increase the recurion limit that python allows.
import time
import random
import sys

#Changed the default recusion limit of python from 1000 times to 100000 times to handle quickSort
sys.setrecursionlimit(10**6)

#inputSize is used in each program to determine the size of our lists.
#This way when we run each version of the program we only need to change
#The value of inputSize
inputSize = 10000
mylist = [0]*inputSize

#Boolean value to determine which type of list to build.
preSorted = True
randomTenth = False
allRandom = False
properBuild = True #This ensures that one of the three build were selected. 

#Boolean value to determine which sorting algorithim
selectionSortBool = False
insertionSortBool = False
bubbleSortBool = False
bubbleWithCountBool = False
quickSortBool = False
mergeSortBool = True

#Function Definitions

#Code for selection sort found on GeeksForGeeks.com
def selectionSort(mylist):
    
        # Traverse through all array elements 
        for i in range(len(mylist)): 
      
        # Find the minimum element in remaining  
        # unsorted array 
            min_idx = i
        
            for j in range(i+1, len(mylist)): 
                if mylist[min_idx] > mylist[j]: 
                    min_idx = j 
              
        # Swap the found minimum element with  
        # the first element         
            mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]

   
def insertionSort(mylist):
        # Traverse through 1 to len(arr) 
        for i in range(1, len(mylist)): 
  
            key = mylist[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
            j = i-1
            while j >=0 and key < mylist[j] : 
                    mylist[j+1] = mylist[j] 
                    j -= 1
            mylist[j+1] = key 


def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Bubble sort with swaps counted modified from our bubble sort code above.
def bubbleSortWithCount(arr):
    n = len(arr)
    swaps = 0
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        if(swaps == 0):
            break
        
      
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)  
        
def mergeSort(nlist):
    #print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",nlist)

                
#Selection structures to build our list.
if(preSorted == True):
    
    print("Sorted list with " + str(inputSize) + " elements.")
    
    for i in range(0,inputSize):
        mylist[i]=i+1
 
#For loop to make an almost sorted list with every tenth value being random.      
elif(randomTenth == True):
    
    print("Partially sorted list with " + str(inputSize) + " elements.")
    
    for i in range(0,inputSize):
        if((i+1)%10 == 0):
            mylist[i]=(random.randint(1,10001))
        else:
            mylist[i]=i+1
            
#For loop to create a completely random list.   
elif(allRandom == True):
    
    print("Completely random list with " + str(inputSize) + " elements.")
    
    for i in range(0,inputSize):
        mylist[i]=(random.randint(1,10001))

#If a type of build is not selected the program will not allow the next if statement to go through.
else:
    print("A list build must be selected in order to run.")
    properBuild = False
    
if(properBuild == True):
    
    if(selectionSortBool == True):
        #Starting Timer
        begin = time.time()
        
        selectionSort(mylist)
        
        end = time.time()
        total = end - begin
        
        print("With the given list Selection Sort took " + str(total) + " seconds.")
        
    elif(insertionSortBool == True):
        #Starting Timer
        begin = time.time()
        
        insertionSort(mylist)
            
        end = time.time()
        total = end - begin 
            
        print("With the given list Insertion Sort took " + str(total) + " seconds.")
        
    elif(bubbleSortBool == True):
        #Starting Timer
        begin = time.time()
        
        bubbleSort(mylist)
            
        end = time.time()
        total = end - begin 
            
        print("With the given list Bubble Sort took " + str(total) + " seconds.")
        
    elif(bubbleWithCountBool == True):
        #Starting Timer
        begin = time.time()
        
        bubbleSortWithCount(mylist)
            
        end = time.time()
        total = end - begin 
            
        print("With the given list Bubble Sort with swaps counted took " + str(total) + " seconds.")
        
        
    elif(quickSortBool == True):
        #Starting Timer
        begin = time.time()
        
        quickSort(mylist, 0, len(mylist)-1)
            
        end = time.time()
        total = end - begin 
            
        print("With the given list Quick Sort took " + str(total) + " seconds.")
        
    elif(mergeSortBool == True):
        #Starting Timer
        begin = time.time()
        n = len(mylist)
        mergeSort(mylist)
            
        end = time.time()
        total = end - begin 
            
        print("With the given list Merge Sort took " + str(total) + " seconds.")
        
    else:
        print("No sorting method was selected.")
        exit()
        



