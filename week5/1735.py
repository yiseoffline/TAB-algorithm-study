import math

nume1, deno1 = map(int, input().split())
nume2, deno2 = map(int, input().split())

res_nume = nume1*deno2 + nume2*deno1
res_deno = deno1*deno2

gcd = math.gcd(res_nume,res_deno)

res_nume = res_nume/gcd
res_deno = res_deno/gcd

print(int(res_nume), int(res_deno))