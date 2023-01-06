# 소수 찾기
# 어떤 소수도 N의 제곱근보다 큰 수로 나눠지지 않는다는 규칙이 있다.

# 입력 받기
n = int(input())
nums = list(map(int, input().split()))
cnt = 0


def sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for num in nums:
    if num <= 1:
        continue
    if sosu(num):
        cnt += 1
print(cnt)
