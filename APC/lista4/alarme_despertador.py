h1, m1, h2, m2 = map(int, input().split())

while h1 != 0 or m1 != 0 or h2 != 0 or m2 != 0:
    total =  (h2 * 60 + m2) - (h1 * 60 + m1)
    if total <= 0:
        total += 1440
    print(total)
    h1, m1, h2, m2 = map(int, input().split())

