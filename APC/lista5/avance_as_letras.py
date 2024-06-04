def subordinarios(A,B):
    return ord(B) - ord(A) 

T = int(input())

for _ in range(T):
    A, B = input().split()
    total = 0
    for i in range(len(A)):
        subtracao = subordinarios(A[i],B[i])
        if subtracao < 0:
            subtracao += 26
        total += subtracao
    print(total)


                
