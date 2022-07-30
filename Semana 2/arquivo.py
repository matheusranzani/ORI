#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Matheus
# Uso básico de arquivos

arquivo = open('/etc/passwd')

# conteudo = arquivo.read()
linha = int(input('Qual a linha que quer ver? '))

for i in range(linha):
    conteudo = arquivo.readline()

print(conteudo)

arquivo.close()
