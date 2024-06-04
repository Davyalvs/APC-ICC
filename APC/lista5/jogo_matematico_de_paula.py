N = int(input())

for _ in range(N):

    X = input()

    num1 = int(X[0])
    num2 = int(X[2])
    charac = X[1]

    if num1 == num2:
        print(num1*num2)
    elif charac in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(num2-num1)
    elif charac in "abcdefghijklmnopqrstuvwxyz":
        print(num1+num2)