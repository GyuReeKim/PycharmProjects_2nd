def bfs(i, j, n):
    global cnt
    q = []

    q.append((i, j))
    visited[i][j] = n
    cnt += 1

    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if land[ni][nj] == '1':
                    q.append((ni, nj))
                    visited[ni][nj] = n
                    cnt += 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
land = [list(input()) for _ in range(N)]
# print(land)

visited = [[0]*N for _ in range(N)]
num = 0
house = []
for i in range(N):
    for j in range(N):
        if land[i][j] == '1' and visited[i][j] == 0:
            num += 1
            cnt = 0
            bfs(i, j, num)
            house.append(cnt)
house = sorted(house)
print(num)
for h in house:
    print(h)
