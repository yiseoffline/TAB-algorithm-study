# 16499

n=int(input())
arr=[]
s = set()

for i in range(n):
    word = tuple(sorted(input()))
    s.add(word)
    
print(len(s))

'''
# 16499

n=int(input())
arr=[]

for i in range(n):
    word = sorted(list(input()))
    if word not in arr:
        arr.append(word)
print(len(arr))
'''