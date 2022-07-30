try:
    arquivo_texto = open('pg5710.txt')
except IOError as excecao:
    print(f'Erro ao acesso: {excecao}')
else:
    acabou_o_arquivo = False
    linha = 0
    while not acabou_o_arquivo:
        linha += 1
        uma_linha = arquivo_texto.readline()
        acabou_o_arquivo = not uma_linha
        if 'lengthened' in uma_linha:
            print(uma_linha + f'(linha {linha})')
            break
    arquivo_texto.close()
