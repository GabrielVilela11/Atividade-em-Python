# --------------------------------------------------EXERCÍCIO --------------------------------------------------------


p1 = 0 #variaveis de cada conjunto de sorvete
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0
valores = []


print("\n *  Bem vindo(a) a sorveteria do Gabriel da Silva Vilela! * \n")
print('~' * 44, " MENU ", '~' * 44)
print("| CÓDIGO |       DESCRIÇÃO       | TAMANHO P(500 ml) | TAMANHO M(1000 ml) | TAMANHO G(2000 ml) |")
print("|   TR   | Sabores tradicionais  |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |")
print("|   ES   |   Sabores especiais   |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |")
print("|   PR   |    Sabores premium    |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |")
print('~' * 96, )

while True: # uso do while True para continuar repitindo até a ordem de parada
    tamanho = input("Digite o tamanho desejado (P/M/G): ")
    codigo = input("Digite o código desejado (TR/ES/PR): ")

    if tamanho == 'P':
        if codigo == 'TR':
            p1 = 6
            print(f"Você pediu um sorvete P com o sabor TRADICIONAL, valor de R${p1},00 ")
            print("~" * 64)
            valores.append(p1)

        elif codigo == 'ES':
            p2 = 7
            print(f"Você pediu um sorvete P com o sabor ESPECIAL, valor de R${p2},00 ")
            print("~" * 61)
            valores.append(p2)

        elif codigo == 'PR':
            p3 = 8
            print(f"Você pediu um sorvete P com o sabor PREMIUM, valor de R${p3},00 ")
            print("~" * 60)
            valores.append(p3)

        else:
            print("!!! CÓDIGO INVÁLIDO !!!\n")
            continue

    elif tamanho == 'M':
        if codigo == 'TR':
            p4 = 10
            print(f"Você pediu um sorvete M com o sabor TRADICIONAL, valor de R${p4},00 ")
            print("~" * 65)
            valores.append(p4)

        elif codigo == 'ES':
            p5 = 12
            print(f"Você pediu um sorvete M com o sabor ESPECIAL, valor de R${p5},00 ")
            print("~" * 62)
            valores.append(p5)

        elif codigo == 'PR':
            p6 = 14
            print(f"Você pediu um sorvete M com o sabor PREMIUM, valor de R${p6},00 ")
            print("~" * 61)
            valores.append(p6)

        else:
            print("!!! CÓDIGO INVÁLIDO !!!\n")
            continue

    elif tamanho == 'G':
        if codigo == 'TR':
            p7 = 18
            print(f"Você pediu um sorvete G com o sabor TRADICIONAL, valor de R${p7},00 ")
            print("~" * 65)
            valores.append(p7)

        elif codigo == 'ES':
            p8 = 21
            print(f"Você pediu um sorvete G com o sabor ESPECIAL, valor de R${p8},00 ")
            print("~" * 62)
            valores.append(p8)

        elif codigo == 'PR':
            p9 = 24
            print(f"Você pediu um sorvete G com o sabor PREMIUM, valor de R${p9},00 ")
            print("~" * 61)
            valores.append(p9)

        else:
            print("!!! CÓDIGO INVÁLIDO !!! \n")
            continue
    else:
        print("!!! TAMANHO INVÁLIDO !!! \n")
        continue


    continuar = input("Deseja fazer outro pedido? (S/N): ") #apos fazer o pedido, usa essa variavel para saber se o cliente deseja continuar ou não
    if continuar == "S":
        continue # Volta do inicio,refazendo todo o processo novamente

    elif continuar == "N":
        total = sum(valores)
        print(f"O total a pagar ficou em: R${total},00 \n")
        print("Encerrando o programa, aguarde...")
        break # usado para interromper o while True
