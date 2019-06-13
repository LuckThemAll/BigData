f = open("C:/Users/Artem/Desktop/BigData/lab3/graph_small.txt", 'r')
matrix = {}
visited = {}
comps = []


def dfs(v):
    visited[v] = True
    for to in matrix[v]:
        if not visited[to]:
            dfs(to)


def find_comps():
    res = 0
    for value in visited:
        if not visited[value]:
            res += 1
            dfs(value)
    return res


for line in f:
    id, vals = line.split(":")
    matrix[int(id)] = []
    visited[int(id)] = False
    for val in vals.split(","):
        matrix[int(id)].append(int(val))
        if int(val) not in matrix:
            matrix[int(val)] = []
            matrix[int(val)].append(int(id))
        else:
            if int(id) not in matrix[int(val)]:
                matrix[int(val)].append(int(id))
        visited[int(val)] = False

print(find_comps())
