'''
Insertion
Quick
Tim
'''
arreglo = [2, 23, 1, 14, 7, 9, 20]
arreglon = [2, 3, 45, 14, 88, 10, 22, 8]
arreglito = [6, 9, 1, 15, 70, 12, 89, 100]

#Merge Sort Alg
def mergeSortAlg(array):  #Divide y venceras Typo
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
           
def insertionSort(array):
    
    
    return array     
                
#print(bubbleSort(arreglo))   
#print(mergeSortAlg(arreglo))



