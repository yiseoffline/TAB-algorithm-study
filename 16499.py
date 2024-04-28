# 16499

n=int(input())
arr=[]

for i in range(n):
    word = sorted(list(input()))
    if word not in arr:
        arr.append(word)
print(len(arr))