# 백준 7569번

M, N, H = map(int, input().split())

box = [[list(input().split()) for i in range(N)] for h in range(H)]
print(box)

for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                pass