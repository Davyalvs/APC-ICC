N = int(input())

for _ in range(N):
    X = input()
    ans = ""

    if len(X) == 1:
        print(X)
    else:
        for i in range(1,len(X)):
            if (i-1) == 0 and X[i-1] in "abcdefghijklmnopqrstuvwxyz":
                ans += X[i-1]
            if X[i] in "abcdefghijklmnopqrstuvwxyz" and X[i-1] == " ":
                ans += X[i]
        print(ans)

