from sys import *
from FileManager import *
from BFS import *
from DFS import *
from AStar import *

def GenerateSolution(rowNumber, colNumber):
    array = []
    number = 1
    for i in range(0, rowNumber):
        row = []
        for j in range(0, colNumber):
            row.append(number)
            number += 1
        array.append(row)
    array[rowNumber-1][colNumber-1] = 0
    return array


if (len(argv) != 6):
    print('The number of arguments is incorrect')

strategyName = argv[1]
strategyParameter = argv[2]
file = FileManager(argv[3])
solutionFilename = argv[4]
infoFilename = argv[5]

file.readFile()
solution = GenerateSolution(file.rowNumber, file.colNumber)

if(strategyName == 'bfs'):
    solver = BFS(file.array, solution, strategyParameter)

elif(strategyName == 'dfs'):
    solver = DFS(file.array, solution, strategyParameter)

elif(strategyName == 'astr'):
    solver = AStar(file.array, solution, strategyParameter)        
else:
    print('Invalid strategy name')
    exit()	
path, visited, processed, maxDepth, solvingTime = solver.solve()
print(path)
if(path != -1):
    file.writeSolution(solutionFilename, path)
    file.writeInfo(infoFilename, len(path), visited, processed, maxDepth, solvingTime)
else:
    file.writeNotFound(solutionFilename)
    file.writeInfo(infoFilename, path, visited, processed, maxDepth, solvingTime)