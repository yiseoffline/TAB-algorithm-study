n = int(input())
sum = 0
result = 0
 
for i in range(1, n + 1):
    sum = sum + i
    result = i
    if sum > n:
        result = result - 1
        break
 
print(result)