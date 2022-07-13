# Write a Python program that determines the location of a saddle point of matrix if one
# exists. An m x n matrix is said to have a saddle point if some entry a[i][j] is the smallest
# value in row i and the largest value in j.

import random


def return_max(l):
    max_val = l[0]
    for i in l:
        if max_val < i:
            max_val = i
    return max_val


def return_min(l):
    min_val = l[0]
    for i in l:
        if min_val > i:
            min_val = i
    return min_val


def find_saddle_point(matrix):
    row_min = []
    col_max = []

    row_count = len(matrix)
    col_count = len(matrix[0])

    for i in range(row_count):
        row_min.append(return_min(matrix[i]))

    for col in range(col_count):
        max_col_value = matrix[0][col]
        for row in range(row_count):
            if matrix[row][col] > max_col_value:
                max_col_value = matrix[row][col]
        col_max.append(max_col_value)

    print(row_min, col_max)

    for row in range(row_count):
        for column in range(col_count):
            if row_min[row] == col_max[column]:
                return (
                    f"Saddle point at {row} {column} for value {matrix[row][column]}."
                )
        return "No Saddle point exist!"


m = [[random.randint(-10, 10) for i in range(2)] for i in range(3)]

print(m)

print(find_saddle_point(m))
