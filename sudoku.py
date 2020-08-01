import csv
import random
import timeit


def read():
    with open('Sudoku.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        temp = []
        for row in csv_reader:
            if line_count is not 0:
                temp.append(row[0].split(';'))
            line_count += 1
        return temp


def get(difficulty):
    llist = []
    for row in read():
        if(float(row[1]) == difficulty):
            llist.append(row[2])

    num = random.randint(0, len(llist)-1)
    return llist[num]


def findCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def validMoves(grid, i, j, e):
    checkRow = all([e != grid[i][x] for x in range(9)])
    if checkRow:
        checkCol = all([e != grid[x][j] for x in range(9)])
        if checkCol:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            # floored quotient should be used here.
            secTopX, secTopY = 3 * (i//3), 3 * (j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    i, j = findCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if validMoves(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo move for backtracking
            grid[i][j] = 0
    return False


def main(difficulty=0):
    if difficulty < 0 or difficulty > 9:
        return "difficulty not define"

    string = get(difficulty)
    llist = []
    for i in range(9):
        ll = []
        for j in range(9):
            letter = string[i*9+j]
            if(letter == '.'):
                ll.append(0)
            else:
                ll.append(int(letter))
        llist.append(ll)
    # print(llist)
    solveSudoku(llist)
    for l in llist:
        print(l)
    return llist


start = timeit.default_timer()
main(9)
stop = timeit.default_timer()
print('Time: ', stop - start)

# call for difficulty 1
# print(main(1))     #call for difficulty 2
# print(main(2))
# print(main(3))
# print(main(4))
# print(main(5))
# print(main(6))
# print(main(7))
# print(main(8))
# print(main(9))     #call or difficulty 9
