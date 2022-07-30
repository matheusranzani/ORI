#!/usr/bin/python3
# Matheus
# Leitura de arquivo binário

arquivo = open('novo', 'wb')

valor = 100
valor_bytes = valor.to_bytes(4, 'big')
print(valor, valor_bytes)
arquivo.write(valor_bytes)

valor = 200
valor_bytes = valor.to_bytes(4, 'big')
print(valor, valor_bytes)

arquivo.write(valor_bytes)

arquivo.close()
