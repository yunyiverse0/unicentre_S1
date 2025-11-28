# 정수 N을 입력받아 아래와 같이 N x N 크기 행렬을 출력하는 프로그램을 작성하시오. 
# 해당 행렬은 배열의 각 행과 열의 번호의 차를 값을 원소로 갖는다.

N = int(input())
a = 2

for i in range(N):
    for j in range(a, N + a):
        print(j,end=" ")
    a += 1
    print()
