from time import sleep

res = '\033[33m'  # Cor amarela
nrm = '\033[0;0m'  # Cor Padrão


def soma(num1, num2):
    resultado = num1 + num2
    print()
    print(f'{res}O resultado é {resultado}{nrm}')
    print()
    sinal = '+'
    historico(num1, num2, resultado, sinal)


def subtracao(num1, num2):
    resultado = num1 - num2
    print()
    print(f'{res}O resultado é {resultado}{nrm}')
    print()
    sinal = '-'
    historico(num1, num2, resultado, sinal)


def multiplicacao(num1, num2):
    resultado = num1 * num2
    print()
    print(f'{res}O resultado é {resultado}{nrm}')
    print()
    sinal = '*'
    historico(num1, num2, resultado, sinal)


def divisao(num1, num2):
    try:
        resultado = num1 / num2
        print()
        print(f'{res}O resultado é {resultado:.2f}{nrm}')
        print()
        sinal = '/'
        historico(num1, num2, resultado, sinal)
    except ZeroDivisionError:
        print()
        print('Não é possível dividir por zero')
        print()


def potencia(num1, num2):
    resultado = num1 ** num2
    print()
    print(f'{res}O resultado é {resultado}{nrm}')
    print()
    sinal = '^'
    historico(num1, num2, resultado, sinal)


def raiz(num1, num2):
    resultado = num1 ** (1 / num2)
    print()
    print(f'{res}O resultado é {resultado:.2f}{nrm}')
    print()
    sinal = 'raiz'
    historico(num1, num2, resultado, sinal)


def hexa():
    while True:
        try:
            num1 = float(input('Digite um número: '))
            int_num1 = int(num1)
            hex_num1 = hex(int_num1).split('x')[-1]
            print(hex_num1)
            break
        except ValueError:
            print(f'{res}Digite apenas números{nrm}')


def media():
    quant = int(input('Qual a quantidade de notas? '))
    notas = 0
    for i in range(0, quant):
        notas += int(input("Digite a nota " + str(i + 1) + ": "))
    media = notas / quant
    print(f'A média é {media}')


def num():
    while True:
        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número:  '))
            return num1, num2
            break
        except ValueError:
            print(f'{res}Digite apenas números{nrm}')


def historico(num1, num2, resultado, sinal):
    try:
        with open('historico.csv', 'a') as arquivo:
            arquivo.write(f'{num1},{num2},{resultado},{sinal}\n')
    except Exception as error:
        print('Um erro inesperado ocorreu!')
        print(error)


def mostrar_historico():
    try:
        with open('historico.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                numeros = linha.strip().split(',')
                print(f'{res}{numeros[0]} {numeros[3]} {numeros[1]} = {numeros[2]}{nrm}')
    except FileNotFoundError:
        print('---------------')
        print('Histórico Vazio')
    except Exception as error:
        print('Um erro inesperado ocorreu!')
        print(error)


def menu():
    print \
        ("""-------------------------
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potência
6 - Raiz
7 - Histórico
8 - Decimal para Hexadecimal
9 - Menu Escola
0 - Fechar programa
-------------------------""")


def menu_escola():
    print \
        ("""------------------------
1 - Cálculo de Média
2 - IMC
0 - Voltar para o menu
------------------------""")


while True:
    menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        num1, num2 = num()
        soma(num1, num2)
    elif opcao == '2':
        num1, num2 = num()
        subtracao(num1, num2)
    elif opcao == '3':
        num1, num2 = num()
        multiplicacao(num1, num2)
    elif opcao == '4':
        num1, num2 = num()
        divisao(num1, num2)
    elif opcao == '5':
        num1, num2 = num()
        potencia(num1, num2)
    elif opcao == '6':
        num1, num2 = num()
        raiz(num1, num2)
    elif opcao == '7':
        mostrar_historico()
    elif opcao == '8':
        hexa()
    elif opcao == '9':
        while True:
            menu_escola()
            opcao2 = input('Escolha uma opção: ')
            if opcao2 == '1':
                media()
                break
            if opcao2 == '2':
                pass  # TODO programar o cálculo de IMC
                print(f'{res}Em desenvolvimento...{nrm}')
                sleep(2)
                break
            elif opcao2 == '0':
                break
            else:
                print('Opção inválida')
    elif opcao == '0':
        print(f'{res}Fechando programa{nrm}')
        break
    else:
        print('Opção inválida')
