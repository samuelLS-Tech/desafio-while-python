# Desafio
soma = 0
qtq = 0
media = 0

nota = (input("Digite um número inteiro:"))

while nota != "-1" and nota != "sair":
    if nota:
        qtq += 1
        soma += int(nota)
    nota = (input("Digite um número inteiro:"))
if qtq > 0: 
    media = soma / qtq
    print("A média é:", media)
else: 
    print("Nenhum número foi digitado.")
