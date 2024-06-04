while True:
    try:
        N = int(input())

        Y = list(map(int, input().split()))
        maior = 0

        for i in range(N):
            if i == 0:
                maior = Y[i]
            if Y[i] > maior:
                maior = Y[i]

        if maior < 10:
            print(1)
        elif maior >= 10 and maior < 20:
            print(2)
        else:
            print(3)

    except EOFError:
        break