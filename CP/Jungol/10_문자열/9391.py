a, b = map(int, input().split())

# AM/PM 구분
if a < 12:
    ampm = "AM"
else:
    ampm = "PM"

# 12시간 형식으로 바꾸기 (0시는 12시로 바꿔야 함)
a = a % 12
if a == 0:
    a = 12

# 출력 (시, 분 모두 2자리로)
print(f"{a:02d}:{b:02d} {ampm}")
