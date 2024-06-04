def espaco(X):
    posicoes = []
    last = len(X)
    if X[0] == " ":
        posicoes.append(0)
    for i in range(1,len(X)-1):
        if X[i] == " " and (X[i-1] == " "):
            posicoes.append(i)
    if X[-1] == " ":
        posicoes.append(last-1)
    return posicoes

def informal(X):
    posicoes = []
    string = ''
    for i in range(len(X)):
        if X[i].isdigit():
            for c in string:
                if c.isalpha():
                    posicoes.append(i)
                    break
        if X[i].isalpha() or X[i].isdigit():
            string = string + X[i]
        else:
            string = ''
    return posicoes

def maiuscula(X):
    posicoes = []
    ver = 0
    for i,letra in enumerate(X):
        if letra == ".":
            ver = 1
        if ver == 1 and (letra.islower() or letra.isupper()):
            ver = 0
            continue
        if ver == 0 and letra.isupper() and i > 0:
            posicoes.append(i)

    return posicoes
    
def minuscula(X):
    posicoes = []
    ver = 0
    if X[0].islower() and X[0] != '"':
        posicoes.append(0)
    for i,letra in enumerate(X):
        if letra == ".":
            ver = 1
        if ver == 1 and letra.islower():
            posicoes.append(i)
            ver = 0
        elif ver == 1 and letra.isupper():
            ver = 0
    return posicoes

def pontuacao(X):
    posicoes = []
    simbolos = [',','.','"']
    last = len(X)

    if X[0] == ',' or X[0] == '.':
        posicoes.append(0)
    for i in range(1, len(X) - 1):
        if X[i] in simbolos:
            if X[i-1] == ' ' and X[i+1] == ' ':
                posicoes.append(i)
            elif X[i-1].isalnum() and X[i+1].isalnum():
                posicoes.append(i)
    if X[-1] == ",":
        posicoes.append(last-1)

    return posicoes


X = input()

verEspaco = espaco(X)
verInformal = informal(X)
vermaiuscula = maiuscula(X)
verMinuscula = minuscula(X)
verPontuacao = pontuacao(X)


verifica = 0

if verEspaco:
    if verifica == 0:
        print("NAO")
        verifica = 1
    print("ESPACO EM BRANCO")
    print(*verEspaco)

if verInformal:
    if verifica == 0:
        print("NAO")
        verifica = 1
    print("INFORMAL")
    print(*verInformal)

if vermaiuscula:
    if verifica == 0:
        print("NAO")
        verifica = 1
    print("MAIUSCULA")
    print(*vermaiuscula)

if verMinuscula:
    if verifica == 0:
        print("NAO")
        verifica = 1
    print("MINUSCULA")
    print(*verMinuscula)

if verPontuacao:
    if verifica == 0:
        print("NAO")
        verifica = 1
    print("PONTUACAO")
    print(*verPontuacao)

if verifica == 0:
    print("SIM")