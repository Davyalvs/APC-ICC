def fatorial(N):
    if N < 2:
        return 1
    else:
        return N * fatorial(N-1)

N = int(input())
print(fatorial(N))