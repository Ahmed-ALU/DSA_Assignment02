Graph = [
    [0,1,0,1,0,0],
    [1.0,1,1,1,1],
    [0,1,0,0,1,1],
    [1,1,0,0,0,0],
    [0,1,1,0,0,0],
    [0,1,1,0,0,0]
]

Alpha = ['A', 'B', 'C', 'D', 'E', 'F']

Vnum = int(6)
i = 0
j = 0
def DynamicTrav(InputGraph, I, J):
    global Vnum

    if I == j:
        J += 1
        pass
    if I == 5 and J == 5:
        return

    if I != J and J<=5 and I<=5:
        if InputGraph[I][J] == 1:
            print(f'{Alpha[J]} is visited from {Alpha[I]}')
            return DynamicTrav(InputGraph, I+1, J+1)
        elif InputGraph[I][J] == 0:
            return DynamicTrav(InputGraph, I, J+1)
    elif I != J and J>5:
        return DynamicTrav(InputGraph, I, 0)


DynamicTrav(Graph, 0, 0)
