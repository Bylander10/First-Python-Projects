from random import choice

blacklist = []


def add_num(lista):
    esc_num = choice(lista)
    lista.pop(lista.index(esc_num))
    blacklist.append(esc_num)
    return esc_num


print("Digite '0' quando terminar de digitar os valores")

lista = []
i = 1
while True:
    valor = int(input(f'Digite o {i}º valor: '))
    if valor == 0:
        break
    else:
        i += 1
        lista.append(valor)

print()
print('Digite 0 quando terminar de sortear\n')
ue = None
while ue != '0':
    if lista:
        print(f'sua lista é {lista}')
        num = add_num(lista)
        print(f'o valor tirado foi {num}')
        ue = input('Digite qualquer coisa pra continuar: ')
    else:
        break

print(f'Sua BlackList é {blacklist}')