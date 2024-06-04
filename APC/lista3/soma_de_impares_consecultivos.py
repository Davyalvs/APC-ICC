def somaconsecultivo(X,Y):
    if X%2 != 0:
        X = X + 2
    else:
        X = X + 1
    if Y%2 != 0:
        Y = Y - 2
    else:
        Y = Y - 1
    n = ((Y-X)/2) + 1
    return (X+Y) * n/2

X = int(input())
Y = int(input())
if Y > X:
    aux = X
    X = Y
    Y = aux

print(int(somaconsecultivo(Y,X)))
