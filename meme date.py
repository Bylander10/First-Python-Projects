from random import choice, randint

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']


def criador_de_memes(quantidade):
    lista_de_memes = []

    for i in range(quantidade):
        mes = choice(meses)
        if mes == 'fevereiro':
            dia = randint(1, 28)
        else:
            dia = randint(1, 31)
        ano = randint(2010, 2021)

        meme = dia, mes, ano
        lista_de_memes.append(meme)
    return lista_de_memes


def organizador_de_memes(quantidade):
    lista_normal = criador_de_memes(quantidade)
    lista_int = []
    lista_raw = (str(data[2]) + str(meses.index(data[1]) + 11) + str(data[0] + 10) for data in lista_normal)
    for dado in lista_raw:
        lista_int.append(int(dado))
    lista_final = (lista_normal[lista_int.index(i)] for i in sorted(lista_int, reverse=True))

    return lista_final


quantidade_de_memes = int(input('Digite a quantidade de memes: '))
lista = organizador_de_memes(quantidade_de_memes)

for meme in lista:
    print(f'{meme[0]} de {meme[1]} de {meme[2]}')
