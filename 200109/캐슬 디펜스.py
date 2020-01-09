# 백준 - 17135번


def f(n, m, k):
    if n == k:
        print(archer)
    else:
        for i in range(n, m):
            archer[i] = 1
            f(n+1, m, k)
            archer[i] = 0



N, M, D = map(int, input().split())
board = [list(input().split()) for _ in range(N)]
print(board)

archer = [0]*M
f(0, M, 3)