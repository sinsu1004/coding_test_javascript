# while 문으로 해결

userInput = int(input())
cnt = 0
while userInput >= 0:
    if userInput % 5 == 0:
        cnt += userInput / 5
        print(int(cnt))
        break
    userInput -= 3
    cnt += 1
if userInput < 0:
    print(-1)
