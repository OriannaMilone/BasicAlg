from collections import deque
import math

graph1 = {
'A': ['B', 'G'] ,  
'B': ['A','C', 'D', 'E'] , 
'C': ['B'] , 
'D': ['B'] , 
'E': ['B'] , 
'G': ['H', 'A'] ,
'H': ['I', 'G'] ,
'I': ['H']
}

array1 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

# Busquedas en profundidad
def dfsAlgIterative(graph, ini_nod, obj_nod):
    toExplore = [ini_nod]
    explored = []

    while(True): 
        if(len(toExplore) == 0): # if there is nothing to explore
            print('No solutions')
            return -1
        
        nodo = toExplore[-1] #Selects the last element to be explore (stack)
        
        if(nodo == obj_nod):
            print('This is the goal: ')
            return str(nodo)
        
        toExplore.pop()
        
        if(not(nodo in explored)):
            explored.append(nodo)
            toExplore.extend(reversed(graph.get(nodo))) # as reversed as a stack

def dfsAlgRecursive(graph, toexplore, explored, nodo, goal):
    #base case
    if(nodo == goal):
        print('This is the solution:')
        return str(nodo)
    else:
        toexplore.pop()
        if(not(nodo in explored)):
            explored.append(nodo)
            toexplore.extend(reversed(graph.get(nodo)))
        
        if(len(toexplore) == 0):
            print('No solution')
            return -1
        
        return dfsAlgRecursive(graph, toexplore, explored, toexplore[-1] , goal)

#Busquedas en amplitud
def bfsAlgIterative(graph, ini_node, goal):
    toExplore = deque([ini_node]) #Para implimentar como una cola
    explored = []

    while(True):    
        if(len(toExplore) == 0):
            print('No solution')
            return -1
        
        nodo = toExplore.popleft() 

        if(nodo == goal):
            print('The solution is')
            return nodo
        
        if(not (nodo in explored)):
            explored.append(nodo)
            toExplore.extend(graph.get(nodo))

def bfsAlgRecursive(graph, explored, toExplore, nodo, goal):
    #Caso base:
    if(nodo == goal):
            print('The solution is')
            return nodo
    else: 
        if(len(toExplore) == 0):
            print('No solution')
            return -1
         
        if(not (nodo in explored)):
            explored.append(nodo)
            toExplore.extend(graph.get(nodo))
        
        return bfsAlgRecursive(graph, explored, toExplore, toExplore.popleft(), goal)

#Busqueda binaria
def binaryAlgIterative(array, target):
    p_right = len(array) - 1 #Right pointer            
    p_left = 0  #Left pointer 

    while(p_left <= p_right):  #Pointers shouldn't cross
        mid = (p_left + p_right)//2

        if(array[mid] == target):
            print('The target is on position: ')
            return mid
        elif(array[mid] > target):
            p_right = mid - 1 #Move the pointer
        elif(array[mid] < target):
            p_left = mid + 1
    
    print('Error: There is not such element in the array')
    return -1 
            
def binaryAlgRecursive(array, p_right, p_left ,target):
   mid = (p_left + p_right)//2
   #Base case:
   if(array[mid] == target):
       return mid
   else:
       if(p_left > p_right):
           return -1
       if(array[mid] > target):
            return binaryAlgRecursive(array, mid-1, p_left, target)
       if(array[mid] < target):
            return binaryAlgRecursive(array, p_right, mid+1, target)





lista = ['A']
explorados = []
#print(dfsAlgRecursive(graph1, lista, explorados, 'A', 'I'))
#print(dfsAlgIterative(graph1, 'A', 'I'))


lista2 = deque(['A']) 
#print(bfsAlgRecursive(graph1, explorados, lista2, 'A', 'I'))
#print(bfsAlgIterative(graph1, 'A', 'I'))

#print(binarySAlg(array1, 23))
r = len(array1)-1
print(binaryAlgRecursive(array1, r, 0, 23))