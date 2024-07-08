# Floyd Algorithm
from collections import deque

# N = 정점의 수
def floyd(graph, N):
    path = [[-1]*N for _ in range(N)]

    distances = [[float('inf')]*N for _ in range(N)]
    for i in range(N):
        distances[i][i] = 0
    for node in graph:
        for next_node, distance in graph[node]:
            distances[node][next_node] = distance
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                new_distances = distances[i][k] + distances[k][j]
                if distances[i][j] > new_distances:
                    distances[i][j] = new_distances
                    path[i][j] = k
    return distances, path

def findPath(path, start, goal):
    res = deque([goal])
    node = path[start][goal]
    while node != -1:
        res.appendleft(node)
        node = path[start][node]
    res.appendleft(start)
    return res

graph = {
    0: [(1, 4), (5, 10)],
    1: [(0, 3), (3, 18)],
    2: [(1, 6)],
    3: [(1, 5), (2, 15), (4, 2), (5, 19), (6, 5)],
    4: [(2, 12), (3, 1)],
    5: [(6, 10)],
    6: [(3, 8)]
}

N = 7
distances, path = floyd(graph, N)
for i in range(N):
    for j in distances[i]:
        print(f"%3d"%j, end='')
    print()
print('------------')
for i in range(N):
    for j in path[i]:
        print(f"%3d"%j, end='')
    print()
print('------------')
p = findPath(path, 0, 2)
for i in p:
    print(i, end=' ')
print()
print(distances[0][2])