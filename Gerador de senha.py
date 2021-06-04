
#Gerador básico de senhas seguras, baseado no exemplo do curso de python da Danki code

base = input("Digite a base da sua senha: ")
print("Dica: nunca coloque dados pessoais ou nomes de familiares como senha.")
senha = ""
for letra in base:
    if letra in "Aa" : senha = senha + "4"
    elif letra in "Ee" : senha = senha + "3"
    elif letra in "Ii" : senha = senha + "1"
    elif letra in "Oo" : senha = senha + "0"
    elif letra in "Tt" : senha = senha + "7"
    elif letra in "Ss" : senha = senha + "5"
    elif letra in "Uu" : senha = senha + "%"
    else: senha = senha + letra
print("Sua nova senha segura é:", senha)