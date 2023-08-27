"""
Find longest increasing path solution
"""
def longest_increasing_path(matrix):
    if len(matrix)<=0:
        return "Matrix should not empty"
    rows, columns = len(matrix), len(matrix[0])
    if rows != columns or rows<1 or columns > 200:
        return "nXm not matching length"
    def dfs(y, x):
            val = matrix[y][x]
            return 1 + max(
                dfs(y+1,x) if y < rows - 1 and val > matrix[y+1][x] else 0,
                dfs(y-1,x) if y > 0 and val > matrix[y-1][x] else 0,
                dfs(y,x+1) if x < columns - 1 and val > matrix[y][x+1] else 0,
                dfs(y,x-1) if x > 0 and val > matrix[y][x-1] else 0)
    return max(dfs(y, x) for y in range(rows) for x in range(columns))

# print("enter number of row")
# rows = int(input())
# print("enter number of columns")
# columns = int(input())
# print("enter array data")
# mat = []
# for _ in range(rows):
#     mat.append(list(map(int, input().split())))
# # mat = [[9,9,4],[6,6,8],[2,1,1]]
# m = longest_increasing_path(mat)
# print(m)

print(longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]]))
print(longest_increasing_path([]))
print(longest_increasing_path([[3,4,5],[3,2,6]]))