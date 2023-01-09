from sys import stdin
input = stdin.readline


def division(startX, startY, m):
    global answer
    start = board[startX][startY]
    for i in range(startX, m+startX):
        for j in range(startY, m+startY):
            if board[i][j] != start:
                answer += "("
                for a in range(2):
                    for b in range(2):
                        division(startX+a*m//2, startY+b*m//2, m//2)
                answer += ")"
                return

    answer += str(start)
    return


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
answer = ""
division(0, 0, n)
print(answer)
