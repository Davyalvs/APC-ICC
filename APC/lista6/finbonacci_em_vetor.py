N = int(input())

for _ in range(N):
    fib = [0,1]
    X = int(input())
    if X == 0:
        print(f'Fib({0}) = {0}')
    elif X == 1:
        print(f'Fib({1}) = {1}')
    else:
        aux = 0
        for i in range(1,X):
            aux = fib[i-1] + fib[i]
            fib.append(aux)
        print(f'Fib({X}) = {fib[X]}')


