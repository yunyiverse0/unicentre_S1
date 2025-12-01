A = []

for i in range(100):
    n = int(input())
    if n == -1:
        break
    A.append(n)
    
if len(A) < 3:
    res = A 
else:
    res = A[-3:]

print(*res)
