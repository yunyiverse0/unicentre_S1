# 내가 짠 코드 틀

N = int(input())
a = ' '

for i in range(N):
    for j in range(i):
        print(a,end='')
    for j in range(2*(N - i) - 1):
        print("*",end='')
    print()

# 일반식을 잘 구해야함
# 일반식 = 2*(N - i) - 1


# 지피티가 짜준 코드 틀
N = int(input())

for i in range(N):   
    print(" " * i + "*" * (2 * (N - i) - 1))
