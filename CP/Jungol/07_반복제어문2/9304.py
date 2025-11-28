# 정수 N을 입력받아 1부터 입력받은 정수 N까지의 수 중 3의 배수의 개수를 출력하는 프로그램을 작성하시오.


# 방법 1 - for문 없이 (반복할 필요 없이 그냥 1-N까지의 개수만 알면 되니까)
N = int(input())

count = len(range(3, N+1, 3))
print(count)

# 방법 2 - 시작점을 3으로 바꿔서 출력
N = int(input())
num = []

for i in range(3, N+1, 3):      # 시작을 1부터 하면 1,4,7, 10 ...1부터 시작한 등차수열이 되어버림
    num.append(i)
print(len(num))
