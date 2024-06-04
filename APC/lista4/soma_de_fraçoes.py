def mdc(a,b):
    if b==0:
        return a
    return mdc(b, a%b)

def mmc(a, b):
    return (a * b) // mdc(a, b)

a,b,c,d = map(int, input().split())

divisor = mmc(b,d)
numerador = ((divisor/b)*a) + ((divisor/d)*c)

comum = mdc(numerador, divisor)

print(int(numerador/comum), int(divisor/comum))





   