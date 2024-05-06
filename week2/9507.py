# 9507

def koong(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        memo[n] = koong(n-1, memo) + koong(n-2, memo) + koong(n-3, memo) + koong(n-4, memo)
        return memo[n]

t = int(input())
nums = []
for i in range(t):
    nums.append(int(input()))

for i in nums:
    print(koong(i))
