# 16499

n=int(input())
arr=[]

for i in range(n):
    arr.append(input())

for i in range(n):
    arr[i]=arr[i].sort()

print(arr)