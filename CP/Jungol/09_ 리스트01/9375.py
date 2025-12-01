#리스트 오름차순인지 아닌지 확인

N = int(input())
a = []

for i in range(N):
    n = int(input())
    a.append(n)

if a == sorted(a):
    print("YES")
else:
    print("NO")
