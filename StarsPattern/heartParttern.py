size = 15

# for a in range(int(size / 2), size + 1, 2):
#     for b in range(1, size - a, 2):
#         print(" ", end = "")

#     for b in range(1, a + 1):
#         print("A", end = "")

#     for b in range(1, (size - a) + 1):
#         print(" ", end = "")

#     for b in range(1, a): 
#         print("A", end ="")
    
#     print("")

# for a in range(size, -1, -1):
#     for b in range(a, size):
#         print(" ", end = "")

#     for b in range(1, (a * 2)):
#         print("B", end = "")
#     print("")
#  OS NUMEROS VAO SERVIR APENAS PARA VOCE DETERMINAR A QUATIDADE DE ESPACOS E DE LETRAS E NAO A SUA POSICAO
for a in range(int(size / 2), size + 1, 2):
    # print("")
    # print("######")
    # print(a) # 7
    # print("######")
    # print("")

    ## Primeira coluna esquerda 
    for b in range(1, size - a, 2): # 1 a 8 - 1 = 7 de dois em dois (1, 3, 5, 7) = 4 espacos vazios
        print(" ", end = "")

    for b in range(1, a + 1): # 1 a 8 - 1 = 7 => printa 7 A (Letras)
        print("A", end = "")
    print("") # (Quebra linha) joga a proxima interação pra proxima linha
    
    ## Segunda coluna direita
    # for b in range(1, (size - a) + 1):
    #     print(b)
    #     print("")

    # for b in range(1, a):
    #     print(b)
    #     print("")
    # print("")