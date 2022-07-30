# String
cadeia = 'Computação'
bytes_cadeia = bytes(cadeia, 'utf-8')
print(f'{cadeia} => {bytes_cadeia}')

# Inteiro
inteiro = 100
bytes_inteiro = inteiro.to_bytes(4, 'big', signed=True)
print(f'{inteiro} => {bytes_inteiro}')

# Real
from struct import pack
real = -3.1415
bytes_real = pack('d', real)
print(f'{real} => {bytes_real}')

# String
print(f"{bytes_cadeia} => {bytes_cadeia.decode('utf-8')}")

# Inteiro
print(f"{bytes_inteiro} => {int.from_bytes(bytes_inteiro, 'big', signed = True)}")

# Real
from struct import unpack
print(f"{bytes_real} => {unpack('d', bytes_real)[0]}")

# Criação de um arquivo binário
try:
  arquivo = open("dados.dat", "wb")
except IOError as excecao:
  print(f"Erro de acesso: {excecao}")
else:
  # Gravação dos dados binários
  comprimento = arquivo.write(bytes_cadeia)
  print(f"{comprimento} bytes escritos")
  comprimento = arquivo.write(bytes_inteiro)
  print(f"{comprimento} bytes escritos")
  comprimento = arquivo.write(bytes_real)
  print(f"{comprimento} bytes escritos")

  # Encerramento do acesso ao arquivo
  arquivo.close()
  print()

# Acesso ao arquivo binário
try:
  arquivo = open("dados.dat", "rb")
except IOError as excecao:
  print(f"Erro de acesso: {excecao}")
else:
  bytes_dados = arquivo.read(12)  # 12 bytes da string
  print(bytes_dados.decode("utf-8"))

  bytes_dados = arquivo.read(4)  # 4 bytes do inteiro
  print(int.from_bytes(bytes_dados, "big", signed = True))

  bytes_dados = arquivo.read(8)  # 8 bytes do real
  print(unpack("d", bytes_dados)[0])
