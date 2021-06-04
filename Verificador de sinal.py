
#Programa para a verificar se um número inteiro é positivo ou negativo, retornando um erro caso o usuario digite um valor inválido

numero = input("Digite um numero inteiro: ")
try:
    inum = int(numero)
except:
    print("Digite um valor inteiro válido")
    quit()
if inum > 0:
    print(f"O numero {inum} é positivo")
elif inum == 0:
    print("Igual a zero.")
else:
    print(f"o Número {inum} é negativo")

    