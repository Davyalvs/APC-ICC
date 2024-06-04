N = int(input())

for _ in range(N):
    X = input()
    for i in X[len(X)//2-1::-1]:
        print(i,end="")

    for j in X[len(X):len(X)//2-1:-1]:
        print(j,end="")
    print()
