S, T, F = input().split()
S, T, F = [int(S),int(T),int(F)]

destino = S + T + F

final = destino%24

print(final)