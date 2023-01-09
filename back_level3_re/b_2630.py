from sys import stdin
input = stdin.readline


def division(x, y, n):

    start = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if start != board[i][j]:
                for k in range(2):
                    for l in range(2):
                        division(x+k*n//2, y+l*n//2, n//2)
                return
    answer[start] += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = {1: 0, 0: 0}

division(0, 0, n)
print(answer[0])
print(answer[1])
