def solucao(a, b, c):
    return (b + (b**2 - 4 * a * c)**0.5) / (2 * a)

L, K, T1, T2, H = map(float, input().split())

if L > H:
    print(F"{H:.9f} {H:.9f}")
else:
    F = solucao(1, H + K * (T1 + T2), K * L * T1)
    if L < H:
        print(F"{F:.9f} {F:.9f}")
    else:
        print(F"{H:.9f} {F:.9f}")


