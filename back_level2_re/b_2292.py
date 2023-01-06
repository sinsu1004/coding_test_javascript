# 1  2  8   20   38  62
#   1  6  12  18   24

n = int(input())
dp = [1]

while dp[-1] < n:
    dp.append(dp[-1] + 6 * (len(dp)))
print(len(dp))
