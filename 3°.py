#Escreva um progama que calcule o imposto de renda a parTr de um salário de 
#um funcionário a parTr de da tabela abaixo:
#Sálario IPRF

#Ate 1.500,00 5%
#Acima de 1500,00 até 3.000,00 8%
#Acima de 3.000,00 até 10.000,00 15%
#Acima de 15.000,00 27%

#O programa deverá ao fim imprimir o valor deo imposto devido, o saláriio bruto 
#e o salário com desconto. O programa ainda deverá se repeTr até que o 
#usuário deseje encerra-lo

salario = float(input("insira o sálario:"))

if salario <= 1500:
    imposto = salario * 0.05
    salarioTotal = salario - imposto
    
elif salario > 1500 and salario <= 3000:
    imposto = salario * 0.08
    salarioTotal = salario - imposto
    
elif salario > 3000 and salario <= 10000:
    imposto = salario * 0.15
    salarioTotal = salario - imposto
    
elif salario > 15000:
    imposto = salario * 0.27
    salarioTotal = salario - imposto
    
print(f"Seu sálario é:{salario}, o imposto recebido foi de -{imposto} do seu sálario, seu sálario total foi de:{salarioTotal}")