import sys

s = sys.stdin.readline().strip()

if len(s) % 2 == 0:
    chk = len(s)
else:
    chk = len(s) - 1

while chk > 0:
    i = 0
    ans = 0
    while i + chk <= len(s):
        sum1 = sum2 = 0
        mid = chk // 2 # 부분 문자열의 중간 지점
        for j in range(mid):
            sum1 += int(s[i + j]) # 왼쪽 절반
            sum2 += int(s[i + chk - 1 - j]) # 오른쪽 절반
        if sum1 == sum2: # 값이 같으면 
            ans = chk
            break
        i += 1
    if ans: # 값이 다르면
        break
    chk -= 2

print(ans)
