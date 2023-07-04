from collections import deque

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






lista = ['A']
explorados = []
#print(dfsAlgRecursive(graph1, lista, explorados, 'A', 'I'))
#print(dfsAlgIterative(graph1, 'A', 'I'))


lista2 = deque(['A']) 
#print(bfsAlgRecursive(graph1, explorados, lista2, 'A', 'I'))
#print(bfsAlgIterative(graph1, 'A', 'I'))

