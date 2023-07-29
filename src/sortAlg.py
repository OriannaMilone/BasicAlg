'''
Insertion
Tim
'''
arreglo = [2, 23, 1, 14, 9, 20, 5]
arreglon = [-2, 1, -1, 3, -45, 14, 88, 10, 22, -8]
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

'''         
def insertionSort(array):
   
   for i in range(len(array)):
       key = array[i+1]
       
       i = key - 1
       
       while(i >= 0 | (array[i] < key)):
        if(key < array[i]):
                temp = array[i] 
                array[i] = key
                array[(i+1)] = temp
 
    
   return array     
'''  

#print(quickSort(arreglito, 0, len(arreglito)))
#print(bubbleSort(arreglo))   
#print(mergeSortAlg(arreglo))
