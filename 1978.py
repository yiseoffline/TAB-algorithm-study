# 1978

def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

n=int(input())
nums = list(map(int, input().split()))

count = sum(is_prime(i) for i in nums)
print(count)