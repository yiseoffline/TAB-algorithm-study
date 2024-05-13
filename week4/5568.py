# 5568 카드 놓기

from itertools import permutations

n = int(input())
k = int(input())
arr = []

for _ in range(n):
    arr.append(input())

perm = permutations(arr, k)

cards = set()

for p in perm:
    cards.add(''.join(map(str, p)))

print(len(cards))
