A,B,C = map(int,input().split())
X,Y,Z = map(int,input().split())

al = X//A
co = Y//B
la = Z//C

print(al*co*la)