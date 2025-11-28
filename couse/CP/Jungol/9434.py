three = set()
five = set()
both = set()

for _ in range(6):
    n = int(input())
    if n % 3 == 0 and n % 5 == 0:
        both.add(n)
    elif n % 3 == 0:
        three.add(n)
    elif n % 5 == 0:
        five.add(n)

print('합집합(union):', three.union(five).union(both))
print('교집합(intersection):', both)
