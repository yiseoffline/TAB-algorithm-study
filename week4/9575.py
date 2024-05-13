# 9575 행운의 수

c = int(input())

for _ in range(c):
    result = set()

    n = int(input())
    A = list(map(int, input().split())) 
    m = int(input())
    B = list(map(int, input().split()))
    k = int(input())
    C = list(map(int, input().split()))
    
    for a in A:
        for b in B:
            for c in C:
                sum=a+b+c
                is_lucky = True
                for w in str(sum):
                    if w not in ['5','8']:
                        is_lucky=False
                        break
                if is_lucky:
                    result.add(sum)


    print(len(result))