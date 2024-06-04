N = int(input())

for _ in range(N):
    total = input()
    manha = input()
    almo = input()

    verficador = 0

    for cam in manha:
        if cam not in total:
            verficador = 1

    for caa in almo:
        if caa not in total:
            verficador = 1

    if verficador == 1:
        print("CHEATER")
    else:
        totalnovo = ""
        for cha in total:
            if cha not in manha and cha not in almo:
                totalnovo += cha

        print("".join(sorted(totalnovo)))