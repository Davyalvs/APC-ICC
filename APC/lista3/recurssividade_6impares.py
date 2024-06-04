def impares(N,i):
    if i <= 6:
        print(N)
        impares(N+2,i+1)

X = int(input())
if X%2 == 0:
    X += 1

impares(X,1)