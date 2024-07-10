#faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, 
#leia o seu peso e sua altura e imprima na tela sua condição de acordo com a 
#tabela abaixo

peso = int(input("qual o peso?:"))
high = int(input("qual a altura?:"))

IMC = peso / (high ** 2)

if IMC < 18.5:
    print("você está abaixo do peso")
if (IMC == 18.6 or IMC > 18.6):
    print("você está abaixo do peso")