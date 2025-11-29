N = int(input())

z = ord('Z')   
num = 0       

for i in range(N):            # N = 3, i = 0,1,2
    for j in range(N):        # j = 0..N-1
        if j < N - i:         # 앞쪽 N-i 칸은 알파벳
            print(chr(z), end=' ')
            z -= 1
        else:                 # 나머지는 숫자(연속 증가)
            print(num, end=' ')
            num += 1
    print()
