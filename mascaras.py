# Solicita ao usuário que insira um número.
numero = int(input('Insira um numero: '))

# Solicita ao usuário que insira uma máscara de bits.
mascara = int(input('Insira a mascara: '))

# Define uma função para realizar a operação bitwise AND entre dois números.
def and_mascara(num, mascara):
    return num & mascara

# Executa a operação AND entre o número e a máscara.
numero_and_mascara = and_mascara(numero, mascara)

# Define uma função para realizar a operação bitwise OR entre dois números.
def or_mascara(num, mascara):
    return num | mascara

# Executa a operação OR entre o número e a máscara.
numero_or_mascara = or_mascara(numero, mascara)

# Define uma função para realizar a operação bitwise XOR entre dois números.
def xor_mascara(num, mascara):
    return num ^ mascara

# Executa a operação XOR entre o número e a máscara.
numero_xor_mascara = xor_mascara(numero, mascara)

# Imprime o resultado da operação AND em representação binária.
print(bin(numero_and_mascara))

# Imprime o resultado da operação OR em representação binária.
print(bin(numero_or_mascara))

# Imprime o resultado da operação XOR em representação binária.
print(bin(numero_xor_mascara))