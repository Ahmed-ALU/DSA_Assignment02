graphDict = { # After many trials, I found it is better to use a dictionary
# Using dictinoary in less complex than using 1s and 0s graph. 
    'A' : ['B','D'],
    'B' : ['A', 'C', 'D', 'E', 'F'],
    'C' : ['B','E','F'],
    'D' : ['A', 'B'],
    'E' : ['B', 'C'],
    'F' : ['B', 'C']
}

visitedNodes = set() # to keep track of visited nodes with no change on it.

def DepthFirst(visitedNodes, graph, startNode):
    if startNode not in graph: # If the selected node is not in the graph at all
        print('The node is not in our graph')
        exit(0)
    
    elif startNode in graph and startNode not in visitedNodes:
        print (startNode)
        visitedNodes.add(startNode) # add the visited nodes to the set of visited nodes to keep traking
        # Use Recursion to check the side nodes for each visited nodes 
        for sideNode in graph[startNode]:
            DepthFirst(visitedNodes, graph, sideNode)
            

# Driver Code
DepthFirst(visitedNodes, graphDict, 'C')