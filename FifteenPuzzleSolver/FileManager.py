from sys import exit

class FileManager:
    filename = ''
    colNumber = 0
    rowNumber = 0
    array = []

    def __init__(self, filename):
        self.filename = filename

    def readFile(self):
        self.file_object = open(self.filename, "r")
        with open(self.filename) as f:
            self.rowNumber, self.colNumber = [int(x) for x in next(f).split()]
            for line in f:
                self.array.append([int(x) for x in line.split()])
        self.file_object.close()

        if((self.colNumber * self.rowNumber) != (len(self.array) * len(self.array[0]))):
            print('Invalid array size')
            #exit()
        
        for line in self.array:
            if(len(line) != self.colNumber):
                print('Invalid row size')
                #exit()

    def writeSolution(self, solutionFilename, moves):
        solutionFile = open(solutionFilename, 'w')
        solutionFile.write(str(len(moves)) + '\n')
        solutionFile.write(moves)
        solutionFile.close()

    def writeInfo(self, infoFilename, moves, visited, prcessed, maxDepth, time):
        infoFile = open(infoFilename, 'w')
        infoFile.write(str(moves) + '\n')
        infoFile.write(str(visited) + '\n')
        infoFile.write(str(prcessed) + '\n')
        infoFile.write(str(maxDepth) + '\n')
        infoFile.write(str(time) + '\n')
        infoFile.close()

