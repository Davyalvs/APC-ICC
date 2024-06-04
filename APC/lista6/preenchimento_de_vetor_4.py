pares = []
impares = []
checkpa = 0
checkim = 0

for _ in range(15):
    valor = int(input())

    if checkim != 5 and checkpa != 5:    
        if valor%2 ==0:
            pares.append(valor)
            checkpa += 1
        else:
            impares.append(valor)
            checkim += 1
            
    if checkpa == 5:
        checkpa += 1
        for indice, ans in enumerate(pares):
            print(f'par[{indice}] = {ans}')

    elif checkim == 5:
        checkim += 1
        for indice1, ans1 in enumerate(impares):
            print(f'impar[{indice1}] = {ans1}')



for i in range(5):
    pares.pop(0)
    impares.pop(0)

for indice2, ans2 in enumerate(impares):
    print(f'impar[{indice2}] = {ans2}')
    
for indice3, ans3 in enumerate(pares):
    print(f'par[{indice3}] = {ans3}')






