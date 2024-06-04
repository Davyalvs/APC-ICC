N = int(input())

X = list(map(int, input().split()))
testador = 0

for i in range(N-1):
    if X[i+1] < X[i]:
        testador = i+2
        break

print(testador)