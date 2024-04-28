N_MAX = 20
L_MAX = 20
R_MAX = 20

dp = [[[0] * (R_MAX + 1) for _ in range(L_MAX + 1)] for _ in range(N_MAX + 1)]

t = int(input())

dp[1][1][1] = 1
for i in range(2, N_MAX + 1):
    for j in range(1, i + 1):
        for k in range(1, i + 1):
            dp[i][j][k] = dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] + dp[i - 1][j][k] * (i-2)

for _ in range(t):
    n, l, r = map(int, input().split())
    print(dp[n][l][r])
