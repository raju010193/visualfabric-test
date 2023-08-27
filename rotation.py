"""
Rotate 2D array in 90 degrees
"""
def rotate_90(matrix):
    if len(matrix) <= 1:
        print("N X M not matched")
        return
    n = len(matrix[0])
    if n != len(matrix):
        print("N X M not matched")
        return

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
    display(matrix, n)
def display(matrix,n):
    for i in range(n):
        print(matrix[i])


# A = [[1,2,3],[4,5,6],[7,8,9]]
# A = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
#
# print("enter number of row")
# rows = int(input())
# print("enter number of columns")
# columns = int(input())
# print("enter array data")
# mat = []
# for _ in range(rows):
#     mat.append(list(map(int, input().split())))
# rotate_90(mat)



#  tests= [7,1,5,3,6,4]
rotate_90([[1,2,3],[4,5,6],[7,8,9]])
rotate_90([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15, 14, 12, 16]])
rotate_90([[5,1,9,11],[2,4,8,10],[13,3,6,7]])
rotate_90([])



