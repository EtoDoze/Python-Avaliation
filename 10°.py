#faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, 
#leia o seu peso e sua altura e imprima na tela sua condição de acordo com a 
#tabela abaixo

peso = float(input("qual o peso?:"))
high = float(input("qual a altura?:"))

IMC = peso / (high ** 2)


if IMC < 18.5:
    print("você está abaixo do peso")
elif IMC == 18.6 or IMC <= 24.9:
    print("você está com o peso ideal")
    
elif IMC == 25.0 or IMC <= 29.9:
    print("você está levemente acima do peso")

elif IMC == 30.0 or IMC <= 34.9:
    print("você está com obesidade grau |")

elif IMC == 35.0 or IMC <= 39.9:
    print("você está com obesidade grau ||")

elif IMC >= 40:
    print("você está com obesidade grau |||")
