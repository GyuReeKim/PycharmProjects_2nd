def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for k in range(N+1):
        if adj[v][k] == 1 and visited[k] == 0:
            dfs(k)


def bfs(v):
    visited2[v] = 1
    q.append(v)

    while q:
        v = q.pop(0)
        print(v, end=' ')
        for k in range(N+1):
            if adj[v][k] == 1 and visited2[k] == 0:
                visited2[k] = 1
                q.append(k)


N, M, V = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]

for k in range(M):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1
# print(adj)
visited = [0]*(N+1)

q = []
visited2 = [0]*(N+1)

dfs(V)
print()
bfs(V)