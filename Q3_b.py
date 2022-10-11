from queue import PriorityQueue

# here we have the graph in the shape of matricies
WeigtedGraph = [
    [-1,13,-1,10,-1,-1],
    [13,-1,5,17,20,18],
    [-1,5,-1,-1,22,30],
    [10,17,-1,-1,-1,-1],
    [-1,20,22,-1,-1,-1],
    [-1,18,30,-1,-1,-1]
]

AlphaPet = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    }

AlphaPetX = {
    0:'A',
    1:'B',
    2:'C',
    3:'D',
    4:'E',
    5:'F',
    }

# The Class of our algorithm
class Q3_b:
    # As studied, we have to get the weighted graph matrix, the number of verticies as critical info to start with 
    def __init__(self, nOfVerticies, InputGraph):
        nOfVerticies = 6 #Default of 6 for our graph
        self.Wgraph = InputGraph
        self.vN = nOfVerticies
        self.visitedNodes = list(['C']) # For future use to store the visited nodes as a critical operation we have to do every step to keep tracking
    

    def Algorithm(self, startV):
        # Initiating the dictionary/list of the wnated answeres with infinities and 0 for the start node
        shortest_path_list = {'A': float('inf'), 'B': float('inf'), 'C': 0, 'D': float('inf'), 'E': float('inf'), 'F': float('inf')}
    
        # To sort and keep track of the vertices we haven't visited yet
        pqueue = PriorityQueue()
        pqueue.put((0, startV))

        while not pqueue.empty():
            (dist, current_vertex) = pqueue.get()
    
            for sideVertix in range(self.vN):
                # This part is control the letters and numbers in our lists and dictionaries
                if current_vertex in [0,1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    current_vertex = AlphaPetX[current_vertex]
                elif current_vertex not in [0,1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    currentVN = AlphaPet[current_vertex]

                # If I commented that it will be a mess
                """
                The point here that it loops through the distances of each side vertix to see which to go with
                """
                if self.Wgraph[currentVN][sideVertix] != -1:
                    distance = self.Wgraph[currentVN][sideVertix]
                    if sideVertix not in self.visitedNodes:
                        if AlphaPetX[sideVertix] not in self.visitedNodes:
                            self.visitedNodes.append(AlphaPetX[sideVertix])
                        old_cost = shortest_path_list[AlphaPetX[sideVertix]]
                        new_cost = shortest_path_list[current_vertex] + distance
                        if new_cost < old_cost:
                            pqueue.put((new_cost, sideVertix))
                            shortest_path_list[AlphaPetX[sideVertix]] = new_cost
        return shortest_path_list, self.visitedNodes



#################################################
AlgObject = Q3_b(6, WeigtedGraph)
temp, temp02 = AlgObject.Algorithm('C')[0], AlgObject.Algorithm('C')[1]


print('The order to be known : ',temp02)

for key in temp:
    print(f'The shortest distance from C to {key} is : {temp[key]}')