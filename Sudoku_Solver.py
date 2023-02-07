'''
Sudoku_Solver - A basic program to input a sudoku and find all possible solutions

Copyright (C) 20223  Balakrishna Prabhu B. N. <balakrishnaprabhu1999@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
-----------------------------------------------------------------------------------------------------------------------

This program will take in a 9*9 matrix of sudoku as an input and then return the solved sudoku as output.
For that we will use functions.
1) To check weather a number is possible at a position.
    - For that we have to check the row the column and the 3*3 square it belongs to.
    -in order to check which 3*3 square it belong to we will use another function.
2) To find out which 3*3 square the given element belong to.
    - This will take the indices of the element as the input and then return a number from 1 - 9.

    This did not work properly as brute force cannot solve all logic.

    Hence using backtracking and recursion to solve the problem.

-----------------------------------------------------------------------------------------------------------------------
'''


def show_sudoku():
    # print('')
    for y in range(9):
        for x in range(9):
            print(matrix[y][x], end='  ')
        print('')


def get_sudoku():
    print('Please enter the sudoku.(not Comma separated eg:123456789 )')
    sudoku = [[] for j in range(9)]
    for i in range(9):
        sudoku[i] = list(map(int, list(input('Row ' + str(i + 1) + ' : '))))
    return sudoku


def possible(number, y, x):
    # returns true if possible.

    # Checking Row.
    for row in range(9):
        if matrix[row][x] == number:
            return False

    # Checking Column.
    for column in range(9):
        if matrix[y][column] == number:
            return False

    # Checking Small Square.
    x_0 = x // 3 * 3
    y_0 = y // 3 * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[y_0 + i][x_0 + j] == number:
                return False
    return True


def solve():
    global matrix
    for y in range(0, 9):
        for x in range(0, 9):
            if matrix[y][x] == 0:
                for num in range(1, 10):
                    if possible(num, y, x):
                        matrix[y][x] = num
                        solve()
                        matrix[y][x] = 0
                return
    global num_sol
    num_sol += 1
    print('Solution Number :', num_sol)
    show_sudoku()

    # input('More?')
    print('')

# Below are some matrix made for testing purposes so that we need not type in each time.
mat = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
       [6, 8, 0, 0, 7, 0, 0, 9, 0],
       [1, 9, 0, 0, 0, 4, 5, 0, 0],
       [8, 2, 0, 1, 0, 0, 0, 4, 0],
       [0, 0, 4, 6, 0, 2, 9, 0, 0],
       [0, 5, 0, 0, 0, 3, 0, 2, 8],
       [0, 0, 9, 3, 0, 0, 0, 7, 4],
       [0, 4, 0, 0, 5, 0, 0, 3, 6],
       [7, 0, 3, 0, 0, 8, 0, 0, 0]]  # mat1
mat2 = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]  # mat2
mat3 = [[5, 0, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 0, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]  # mat3
mat3solved = [[5, 3, 4, 6, 7, 8, 1, 9, 2],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 9, 7, 1],
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]]  # mat3solved
empty_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
mat4 = [[0, 0, 0, 0, 0, 0, 0, 0, 8],
        [6, 0, 0, 4, 7, 0, 0, 0, 0],
        [0, 7, 4, 9, 0, 0, 6, 2, 0],
        [5, 0, 0, 0, 2, 0, 0, 3, 0],
        [7, 0, 6, 0, 0, 0, 8, 0, 4],
        [0, 8, 0, 0, 9, 0, 0, 0, 6],
        [0, 6, 1, 0, 0, 7, 5, 8, 0],
        [0, 0, 0, 0, 6, 8, 0, 0, 2],
        [8, 0, 0, 0, 0, 0, 0, 0, 0]]
mat5 = [[1, 0, 0, 0, 0, 3, 0, 0, 5],
        [5, 0, 0, 0, 0, 8, 6, 0, 7],
        [0, 0, 0, 0, 0, 0, 4, 1, 0],
        [0, 7, 8, 0, 0, 6, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 3, 0, 0, 8, 5, 0],
        [0, 3, 4, 0, 0, 0, 0, 0, 0],
        [9, 0, 2, 7, 0, 0, 0, 0, 1],
        [7, 0, 0, 9, 0, 0, 0, 0, 4], ]

mat6 = [[9, 2, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 7, 3, 0, 0, 6, 0, 9],
        [0, 9, 8, 0, 6, 0, 0, 0, 0],
        [0, 0, 4, 2, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 8, 6, 0],
        [4, 0, 9, 0, 0, 2, 5, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 4, 2]]

num_sol = 0

#matrix = get_sudoku()
matrix = empty_matrix

print('Question :: ')
show_sudoku()
print('')
solve()
print('Done')
