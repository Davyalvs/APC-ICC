# numero primo
# N = int(input())

# for i in range(N):
#     contador = 0
#     X = int(input())
#     for i in range(1,X+1):
#         if X%i == 0:
#             contador += 1
#     if contador == 2:
#         print(f'{X} eh primo')
#     else:
#         print(f'{X} nao eh primo')







# numero perfeito
# N = int(input())

# for i in range(N):
#     soma = 0
#     X = int(input())
#     for i in range(1,X):
#         if X%i == 0:
#             soma += i
#     if soma == X:
#         print(f'{X} eh perfeito')
#     else:
#         print(f'{X} nao eh perfeito')




# divisores I
# X = int(input())

# for i in range(1,X+1):
#    if X%i == 0:
#       print(i) 





# sequencias de crescentes
# X = int(input())

# while X != 0:
#     for i in range(1,X+1):
#         if i == X:
#             print(i)
#         else:
#             print(i, end=" ")
#     X = int(input())




# sequencia logica 2
# X, Y = map(int, input().split())
# K = 1
# i = 1

# while i < Y:
#     for _ in range(X):
#         if _ == X-1:
#             print(i)
#         else:
#             print(i, end=" ")
#         i += 1





# sequencia logica
# N = int(input())
# J = 1

# for i in range(1,N+1):
#     print(f'{i} {i*i} {i*i*i}')
#     print(f'{i} {i*i+1} {i*i*i+1}')