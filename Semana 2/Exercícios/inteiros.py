from numpy import random

nome_arquivo = 'inteiros.dat'

try:
    arquivo = open(nome_arquivo, 'wb')
except IOError as exececao:
    print(f'Erro de acesso {exececao}')
else:
    # Inicializa o vetor com números aleatórios de 0 a 100
    inteiros = [random.randint(100) for n in range (20)]
    print(inteiros)

    for inteiro in inteiros:
        inteiro_bytes = inteiro.to_bytes(1, 'big')
        arquivo.write(inteiro_bytes)

    arquivo.close()
