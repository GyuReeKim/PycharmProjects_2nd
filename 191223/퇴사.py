# 푸는중


def f(i):
    global add
    visited[i] = 1
    add += P[i]
    for k in range(1, N+1):
        if adj[i][k] == 1 and visited[k] == 0:
            f(k)


N = int(input())
adj = [[0]*(N+1) for _ in range(N+1)]

T = [0]
P = [0]
for i in range(1, N+1):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    for j in range(1, N+1):
        if j >= i + t:
            adj[i][j] = 1
# print(T)
# print(P)
print(adj)

for i in range(1, N+1):
    for j in range(1, N+1):
       if j + T[j] > N:
           adj[i][j] = 0
print(adj)

maxV = 0
for i in range(1, N+1):
    if i + T[i] <= N:
        visited = [0]*(N+1)
        add = 0
        f(i)
        # print(visited)
        # print(add)
        if add > maxV:
            maxV = add
print(maxV)