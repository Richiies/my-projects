def digits_product(n):
    if n == 0:
        return 0
    p = 1
    while n > 0:
        d = n % 10
        p *= d
        n //= 10
    return p


def max_dp(L, R):
    max_prod = digits_product(L)
    num = L
    for n in range(L+1, R+1):
        p = digits_product(n)
        if p > max_prod:
            mmax_prod = p
            num = n
    return num


T = int(input())
res = []
for i in range(T):
    line = input().split()
    L = int(line[0])
    R = int(line[1])
    res.append(max_dp(L,R))

for n in res:
    print(n)
