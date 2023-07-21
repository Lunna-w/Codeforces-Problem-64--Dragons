s, n = map(int, input().split())

dragons = []

for i in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))

dragons.sort()

for x, y in dragons:
    if s > x:
        s += y
    else:
        print("NO")
        break
else:
    print("YES")