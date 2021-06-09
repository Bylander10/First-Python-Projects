idade = input('Digite a idade do cachorro: ')

print()

try:
    idade = int(idade) * 7

    print(f'A idade humana do cachorro é {idade} anos')
except ValueError:
    idade = idade.split()
    idade = int(idade[0])
    idade = 7 * idade / 12
    ano = int(idade)
    mes = int((idade % 1) * 12)

    print(f'A idade humana do cachorro é {ano} anos e {mes} meses')