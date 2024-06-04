P,C = map(int, input().split())

X = list(map(int, input().split()))
testador = 0

for i in range(C-1):
    if abs(X[i+1] - X[i]) > P:
        testador = 1
        break

if testador == 1:
    print('GAME OVER')
else:
    print('YOU WIN')
