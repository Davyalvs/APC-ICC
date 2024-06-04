x1, y1, x2, y2 = map(int, input().split())
testc = 1


while x1 != 0 or y1 != 0 or x2 != 0 or y2 != 0:
    dentro = 0
    N = int(input())
    for i in range(N):
        xm, ym = map(int, input().split())
        if xm >= x1 and xm <= x2 and ym >= y2 and ym <= y1:
            dentro += 1
    print(f'Teste {testc}')
    print(dentro)
    testc += 1
    x1, y1, x2, y2 = map(int, input().split())

