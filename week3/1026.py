# 1026 보물

n = int(input())
A = list(map(int, input().split()[:n]))
B = list(map(int, input().split()[:n]))
res=0

A.sort()
B.sort(reverse=True)

for i in range(n):
    res += A[i]*B[i]

print(res)