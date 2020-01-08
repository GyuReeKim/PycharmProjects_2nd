# 백준 7569번
# 틀림
# 반례
# 5 3 1
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0

from collections import deque

def f(h, i, j):
    q = deque()

    q.append((h, i, j))
    visited[h][i][j] = 0

    while q:
        h, i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if box[h][ni][nj] == '0' and visited[h][ni][nj] == -1:
                    box[h][ni][nj] = '1'
                    q.append((h, ni, nj))
                    visited[h][ni][nj] = visited[h][i][j] + 1
        for l in range(2):
            nh = h + dh[l]
            if 0 <= nh < H:
                if box[nh][i][j] == '0' and visited[nh][i][j] == -1:
                    box[nh][i][j] = '1'
                    q.append((nh, i, j))
                    visited[nh][i][j] = visited[h][i][j] + 1


dh = [-1, 1]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

M, N, H = map(int, input().split())

box = [[list(input().split()) for i in range(N)] for h in range(H)]
# print(box)

visited = [[[-1]*M for i in range(N)] for h in range(H)]
# print(visited)

for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == '1' and visited[h][i][j] == -1:
                f(h, i, j)
# print(box)
# print(visited)

result = 0
maxV = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == '0':
                result = -1
            if visited[h][i][j] > maxV:
                maxV = visited[h][i][j]
            if result == -1:
                break
        if result == -1:
            break
    if result == -1:
        break
if result == -1:
    print(result)
else:
    print(maxV)