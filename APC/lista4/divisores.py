def menor(A, B, C, D, n):
    if n > max(A, B, C, D):
        return -1
    elif n % A == 0 and n % B != 0 and C % n == 0 and D % n != 0:
        return n
    else:
        return menor(A, B, C, D, n + 1)

A, B, C, D = map(int, input().split())

print(menor(A, B, C, D, 1))





# para = 0
# for n in range(1, max(A, B, C, D) + 1):
#     if n % A == 0 and n % B != 0 and C % n == 0 and D % n != 0:
#         print(n)
#         para = 1
#         break

# if para == 0:
#     print(-1)

