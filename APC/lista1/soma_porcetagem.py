A,B = input().split()
A,B = [float(A),float(B)]

X = B - A
aumento = (X/A)*100

print(f'{aumento:.2f}%')