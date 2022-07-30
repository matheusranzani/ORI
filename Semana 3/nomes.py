# Criação de um arquivo binário
try:
  arquivo = open("nomes.dat", "wb")
except IOError as excecao:
  print(f"Erro de acesso: {excecao}")
else:
  # Entrada de dados até linha vazia
  nome = input("Nome: ")
  while nome != "":
    # Conversão e gravação
    bytes_nome = bytes(nome, "utf-8")
    comprimento = arquivo.write(bytes_nome)
    print(f"{comprimento} bytes escritos")

    # Próxima leitura
    nome = input("Nome: ")

  # Encerramento do acesso ao arquivo
  arquivo.close()
  print()
