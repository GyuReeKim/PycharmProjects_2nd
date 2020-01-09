# 백준 - 7569번
from collections import deque


def bfs(h, i, j):
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

q = deque()
visited = [[[-1]*M for i in range(N)] for h in range(H)]


for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == '1':
                q.append((h, i, j))
                visited[h][i][j] = 0
bfs(q[0][0], q[0][1], q[0][2])
# print(box)
# print(visited)

maxV = 0
unripe = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if visited[h][i][j] > maxV:
                maxV = visited[h][i][j]
            if box[h][i][j] == '0':
                unripe = -1
            if unripe == -1:
                break
        if unripe == -1:
            break
    if unripe == -1:
        break
if unripe == -1:
    print(unripe)
else:
    print(maxV)