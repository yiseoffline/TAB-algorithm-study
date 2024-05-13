# 1312 소수
# 10으로 n번까지 나눈 다음에 맨 마지막 숫자 추출
a,b,n = map(int, input().split())

rest = str(a/b)
integer, decimal = rest.split('.')

print(decimal[n-1])