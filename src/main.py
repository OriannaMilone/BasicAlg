from collections import deque
import math
import queue
import heapq

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

graph2 = {
'A': [(3, 'C'), (2, 'F')] ,  
'B': [(6, 'F'), (2, 'G'), (1, 'D'), (2, 'E')] , 
'C': [(3, 'A'), (2, 'F'), (1, 'E'), (4, 'D')] , 
'D': [(1, 'B'), (4, 'C')] , 
'E': [(2, 'B'), (1, 'C'), (3, 'F')] , 
'G': [(5, 'F'), (2, 'B')] ,
'F': [(2, 'A'), (5, 'G'), (6, 'B'), (3, 'E'), (2, 'C')]
}

matrix1 = [[0, 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
          ['A', 0, '', 3, '', '', 2, ''],
          ['B', '', 0, '', 1, 2, 6, 2],
          ['C', 3, '', 0, 4, 1, 2, ''],
          ['D', '', 1, 4, 0, '', '', ''],
          ['E', '', 2, 1, '', 0, 3, ''],
          ['F', 2, 6, 2, '', 3, 0, 5],
          ['G', '', 2, '', '', '', 5, 0],
          ]

array1 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

inf = math.inf

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


def dijkstraAlg(graph, ini_node, goal):
    matrix = {
        ini_node : [False, 0, str(ini_node)] #Matriz (Nodos: [Edo, Dist, Prev])
              }
    for i in graph:
        matrix[i] = [False, inf, '?'] #Incializa la matriz con los nodos y su info

    unexplored= [(0, ini_node)] 
    heapq.heapify(unexplored)   # Cola de prioridad

    while(unexplored):   
        current_distance , node = heapq.heappop(unexplored) #Selecciona elemento con mayor prioridad en la cola
        
        print(f"Seleccionando nodo: {node}, distancia: {current_distance}")
        
        if(node == goal):
            return matrix.get(node) #Devuelve la info del nodo objetivo (True, x, Nx)
        
        if(not(matrix[node][0])):
            matrix[node][0] = True  #El nodo ha sido explorado
            
            for neighbor in graph.get(node):
                distance, nodos = neighbor

                new_distance = current_distance + distance

                if(new_distance < matrix[nodos][1]):
                    matrix[nodos][1] = new_distance
                    matrix[nodos][2] = node
                    heapq.heappush(unexplored, (new_distance, nodos)) #Agrega a la cola de prioridad los elementos
        print(f"Matriz: {matrix}")       
         
    return matrix.get(goal)    

    #

def dijkstraAlg2(matrix, ini_node, goal):
    register = {
                ini_node : [False, 0, ini_node]  #Registra: Estado, Distancia, Nodo Anterior
        }
    for i in range( len(matrix.keys()) -1 ):
            register[list(matrix.keys())[i+1]] = [False, inf, '?']  #Inicializa todos los nodos
    print(register)

    unexplored = [(0, ini_node)] 
    heapq.heapify(unexplored)
   

    while(True):
        print('Vueltas:')
        if(len(unexplored) == 0):
            return -1
        
        priority, node = heapq.heappop(unexplored) #Tomar el nodo con mayor prioridad de la cola
        print(node)

        if(node == goal):
            register[node][0] = True
            return register[node]

        if(not(register[node][0])):
            register[node][0] = True #Marcamos al nodo, como visitado

            for e in range(len(matrix.get(node))):
                heapq.heappush(unexplored, matrix.get(node)[e])   #Agregar los vecino del nodo
                matrix_distance , value = matrix.get(node)[e]   #Vecinos registrados en la tabla
                
                actual_distance = register[value][1]
                new_distance = matrix_distance + register[node][1]  
                
                if(actual_distance > new_distance):
                    register[value][1] = new_distance
                    register[value][2] = node

            print(register)    




lista = ['A']
explorados = []
#print(dfsAlgRecursive(graph1, lista, explorados, 'A', 'I'))
#print(dfsAlgIterative(graph1, 'A', 'I'))

lista2 = deque(['A']) 
#print(bfsAlgRecursive(graph1, explorados, lista2, 'A', 'I'))
#print(bfsAlgIterative(graph1, 'A', 'I'))

#print(binarySAlg(array1, 23))
#print(binaryAlgRecursive(array1, len(array1)-1, 0, 23))

#print(dijkstraAlg(graph2, 'A', 'B'))

print(dijkstraAlg2(graph2, 'A', 'B'))
