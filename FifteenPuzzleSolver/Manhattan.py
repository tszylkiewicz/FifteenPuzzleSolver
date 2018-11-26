from Base import *
from Direction import *
from time import *
from math import ceil

class Manhattan:

    frontier = {}
    explored = {}

    def __init__(self, start, target):
        self.target = target
        self.start = Base(None, start, Direction(1), 0)
        self.maxDepth = 0
        self.rows = len(start)
        self.columns = len(start[0])
        if(self.start.state != self.target):
            distance = self.countDistance(self.start.state)           
            self.frontier.setdefault(distance, []).append(self.start.state)
            self.explored[str(self.start.state)] = self.start     

    def countDistance(self, state):     
        distance = 0
        for x in state:
            for y in x:                
                if(y != 0):
                    temp = y % self.columns
                    if(temp == 0):
                        temp = self.columns
                    distance += abs((state.index(x) + 1) - ceil(y / self.rows)) + abs((x.index(y) + 1) - temp)
        return distance   

    def solve(self):
        startTime = time()
        while(len(self.frontier) > 0):
            closest = min(self.frontier)
            self.currentState = self.frontier[closest].pop(0)
            if(len(self.frontier[closest]) == 0):
                del(self.frontier[closest])
            print(self.frontier)
            self.currentState = self.explored[str(self.currentState)]
            moves = self.currentState.getValidMoves()
            for move in moves:
                newState = Base(self.currentState, self.currentState.move(move), move, self.currentState.pathCost + 1)
                if(newState.pathCost > self.maxDepth):
                    self.maxDepth = newState.pathCost
                if(newState.state == self.target):
                    solvingTime = time() - startTime
                    return newState.getPath(), len(self.explored) + 1, len(self.explored) - len(self.frontier), self.maxDepth, solvingTime
                if(str(newState.state) not in self.explored.keys()):
                    self.explored[str(newState.state)] = newState
                    distance = self.countDistance(newState.state)
                    if(distance not in self.frontier):
                        self.frontier.setdefault(distance, []).append(newState.state)
                    else:
                        self.frontier[distance].append(newState.state)