d = {}

a = int(input())

for i in range(a):
    n, p = input().split()
    n = int(n)
    if n == 1:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    elif n == 2:
        if p in d:
            print(d[p])
            d.pop(p)
        else:
            print(0)
print(d)
