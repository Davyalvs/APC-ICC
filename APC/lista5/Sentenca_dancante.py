def sentenca(sentenca):
    resultado = ''
    maiuscula = True
    for char in sentenca:
        if char.isalpha():
            if maiuscula:
                resultado += char.upper()
            else:
                resultado += char.lower()
            maiuscula = not maiuscula
        else:
            resultado += char
    return resultado

X = input()
print(sentenca(X)) 





