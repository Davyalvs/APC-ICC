T = int(input())

for _ in range(T):
    dic = {}
    M,N = map(int, input().split())
    for i in range(M):
        jap = input()
        trad = input()
        dic[jap] = trad
    
    for j in range(N):
        ans = ""
        texto = list(input().split())
        for palavra in texto:
            if palavra in dic:
                ans += dic[palavra] + " "
            else:
                ans += palavra + " "
        print(ans.rstrip())
    print()
