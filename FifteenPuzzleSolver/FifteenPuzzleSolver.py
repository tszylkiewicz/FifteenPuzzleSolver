from sys import *
from FileManager import *
from functions import *
from BFS import *
from DFS import *
from Manhattan import *
from Hamming import *

if (len(argv) != 6):
    print('The number of arguments is incorrect')
    exit()

strategyName = argv[1]
strategyParameter = argv[2]
file = FileManager(argv[3])
solutionFilename = argv[4]
infoFilename = argv[5]

file.readFile()

solution = GenerateSolution(file.rowNumber, file.colNumber)

if(strategyName == 'bfs'):
    print(strategyName)
    print(strategyParameter)
    solver = BFS(file.array, solution, strategyParameter)

elif(strategyName == 'dfs'):
    print(strategyName)
    print(strategyParameter)
    solver = DFS(file.array, solution, strategyParameter)

elif(strategyName == 'astr'):
    print(strategyName)
    if(strategyParameter == 'hamm'):
        print(strategyParameter)
        solver = Hamming(file.array, solution) 
    elif(strategyParameter == 'manh'):
        print(strategyParameter)
        solver = Manhattan(file.array, solution)         
    else:
        print('Invalid strategy parameter')
        exit()

else:
    print('Invalid strategy name')
    exit()

path, visited, processed, maxDepth, solvingTime = solver.solve()
print(path)
solvingTime = round(solvingTime, 3)
file.writeSolution(solutionFilename, path)
file.writeInfo(infoFilename, len(path), visited, processed, maxDepth, solvingTime)

#print(solutionFilename)
#print(infoFilename)
