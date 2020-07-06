from enum import Enum

class Direction(Enum):
    U = 1   #up  
    D = 2   #down
    L = 3   #left
    R = 4   #right
    N = 5

    def __str__(self):
        return(self.name)
