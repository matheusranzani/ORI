#!/usr/bin/python3
# Matheus
# Criação de arquivo

arquivo = open('novo', 'wb')

valor = 10101010
valorBytes = valor.to_bytes(4, 'big')

print(valor, valorBytes)

arquivo.write(valorBytes)

arquivo.close()
