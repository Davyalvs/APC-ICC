N = int(input())

while N != 0:
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(min(i,j, N-i-1, N-j-1)+1)
        matriz.append(linha)

    for ele in matriz:
        print("  ",end="")
        print('   '.join(map(str,ele)).rstrip())

    
    print()
    N = int(input())