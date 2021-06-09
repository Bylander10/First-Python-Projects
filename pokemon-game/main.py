from pokemon import *

from pessoa import *


def escolher_pokemon_inicial(player):
    print(f'Olá {player}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada')

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print('1 - ', pikachu)
    print('2 - ', charmander)
    print('3 - ', squirtle)

    while True:
        escolha = input('Escolha o seu Pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida, digite apenas os números mostrados')


player = Player('João')
player.capturar(PokemonFogo('charmander', level=1))

inimigo1 = Inimigo(nome='Gary', pokemons=[PokemonAgua('squirtle', level=1)])

player.batalhar(inimigo1)