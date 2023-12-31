
MIN_RUN_SIZE = 32

arreglo = [2, 23, 1, 14, 9, 20, 5]
arreglon = [-2, 1, -1, 3, -45, 14, 88, 10, 22, -8, 12, 4, 56, 16, -5, 15, 27]
arreglito = [6, 9, 1, 15, 70, 12, 89, 100]

#Merge Sort Alg
def mergeSortAlg(array):  #Divide and Conquer Typo
    arrayleft = []
    arrayright = []
    #Base case:
    if(len(array) == 1):
        return array
    #Recursive Case
    else:
        mid = len(array) // 2
        arrayleft = array[:mid]
        arrayright = array[mid:]
      
        arrayOne = mergeSortAlg(arrayleft)
        arrayTwo = mergeSortAlg(arrayright)

        return mergeAlg(arrayOne, arrayTwo)
def mergeAlg(array1, array2):
    array3 = []
    while((len(array1)> 0) and (len(array2)> 0)):

        if(array1[0] < array2[0]):
            array3.append(array1[0])
            array1.remove(array1[0])              
        else: 
            array3.append(array2[0])
            array2.remove(array2[0])
     
    if(len(array1)> 0): 
        array3.append(array1[0])
    if(len(array2)> 0):
        array3.append(array2[0])
    
    return array3

#Bubble Sort Alg   
def bubbleSort(array):
    if(len(array) == 0): 
        return array
    else:
       counter = len(array) 
       while(counter >= 0): 
            pointerOne = 0
            pointerTwo = 1
            
            for i in range(len(array) -1):
                if(array[pointerOne] > array[pointerTwo]):
                    aux = array[pointerTwo]
                    array[pointerTwo] = array[pointerOne]
                    array[pointerOne] = aux
                
                pointerOne = pointerTwo 
                pointerTwo += 1
                
            counter -= 1
       
    return array

#Quick Sort Alg 
def quickSort(array, beg, end): #Divide and Conquer Typo
    array = array[beg:end]
   
    if(len(array) <= 1): 
      return array
    else:    
        pivot = array.pop((len(array)//2)) #Middle element
        i = -1
        for j in range(len(array)):
            if(array[j] < pivot):
                i += 1
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
        array.insert(i+1, pivot)
        return quickSort(array, 0, i+1) + [pivot] +  quickSort(array, i+2, len(array))

#Insertion Sort Alg    
def insertionSort(array):
   for j in range(len(array) -1):
        j += 1
        i = j - 1
        while(i >= 0):
           if(array[j] < array[i]):
               temp = array[i]
               array[i] = array[j]
               array[j] = temp
               i -= 1
               j -= 1
           else:
               break
   return array     

'''
def minRun(n):
    r = 0
    while(n >= MIN_RUN_SIZE):
        r |= n & 1
        n >>= 1
    return n + r

def timSort(array): #Hybrid Alg (Merge and Insertion Sort)
    #run_size = minRun(len(array))
    run_size = 4
    
    for start in range(0, n, run_size):
        end = min(start + run_size - 1, n - 1)
        insertionSort(arr, start, end)
        
    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size
        
    return mergeAlg(a,b) 

print(timSort(arreglon))
'''

#print(insertionSort(arreglito))
#print(quickSort(arreglito, 0, len(arreglito)))
#print(bubbleSort(arreglo))   
#print(mergeSortAlg(arreglo))
