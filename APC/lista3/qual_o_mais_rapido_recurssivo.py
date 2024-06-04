O, B, I = map(float, input().split())

def rapido(A,B):
    if A < B:
        return A
    else:
        return B

menor = rapido(rapido(O,B),I)

aux = 0

if O == menor:
    aux += 1

if B == menor:
    aux += 1

if I == menor:
    aux += 1

if aux >= 2:
    print("Empate")
else:
    if O == menor:
        print("Otavio")
    elif B == menor:
        print("Bruno")
    elif I == menor:
        print("Ian")


    

