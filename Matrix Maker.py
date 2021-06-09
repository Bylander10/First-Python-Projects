"""
04 - leia uma matriz de 4 x 4,imprima a matriz e retorne a localização
(linha e coluna) do maior valor
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = -999

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input("Informe os numeros para a matriz : "))

for impressao_matriz in matriz:
    print(impressao_matriz)

for linha in matriz:
    for maior_valor in linha:
        if maior_valor > 0:
            if maior_valor > maior:
                maior = maior_valor
print(f'o maior número é {maior}')

coordenada = ()
for linha in matriz:
    if maior in linha:
        coordenada = (matriz.index(linha) + 1, linha.index(maior) + 1)

print(f'linha: {coordenada[0]}')
print(f'coluna: {coordenada[1]}')
