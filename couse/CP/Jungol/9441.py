nums = list(map(float, input().split()))
D = {}

for i in nums:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1

for j in D:
    print(f"{j}: {D[j]}")
