def find_smallest_name(*args):
    letras = [len(elemento) for elemento in args]
    index_menor = letras.index(min(letras))
    return args[index_menor]


print('Digite Enter quando acabar de digitar os nomes')
print()
i = 1
nome_digitado = 'nome'
lista_de_nomes = []
while nome_digitado:
    nome_digitado = input(f'Digite o {i}º nome:\n')
    lista_de_nomes.append(nome_digitado)
    i += 1

lista_de_nomes.pop()
print('O menor nome é:')
print(find_smallest_name(*lista_de_nomes))