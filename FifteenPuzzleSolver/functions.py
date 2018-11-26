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
