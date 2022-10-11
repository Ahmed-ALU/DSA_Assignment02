from unittest import result
from test import V


Vnumber =  int(6)

inf = 9999

QuestionGraph = [[0,1,inf,3,2,inf],
                [1,0,1,1,inf,inf],
                [inf,1,0,5,inf,inf],
                [3,1,5,0,3,inf],
                [2,inf,inf,3,0,inf],
                [1,inf,inf,5,2,0]]

def APSP(Inputgraph) -> list:
    """
    The algorithm here is clear and no need for deep explanation
    it is just comparing each edge with the min method to check the shortest path for each
    O(V^3)
    """
    global inf, Vnumber

    ResultGraph = Inputgraph
    for k in range(Vnumber):
        for i in range(Vnumber):
            for j in range(Vnumber):
                ResultGraph[i][j] = min(ResultGraph[i][j],
								ResultGraph[i][k] + ResultGraph[k][j]
								)
                if ResultGraph[i][j] >= 9999:
                    ResultGraph[i][j] = 9999
    
    #printing a good graph
    for i in range(Vnumber):
        for j in range(Vnumber):
            if ResultGraph[i][j] >= 9999:
                ResultGraph[i][j] = 'inf'

    return ResultGraph


# ONLY for printing
counter = int()
print(f'-:  X  Y  Z  W  V    U')
for row in APSP(QuestionGraph):
    if counter == 0:
        print(f'X: {row}')
    elif counter == 1:
        print(f'Y: {row}')
    elif counter == 2:
        print(f'Z: {row}')
    elif counter == 3:
        print(f'W: {row}')
    elif counter == 4:
        print(f'V: {row}')
    elif counter == 5:
        print(f'U: {row}')
    counter+=1

