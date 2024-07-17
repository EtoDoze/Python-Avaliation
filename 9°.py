#Escreva um programa que recebe um CPF e verifica se ele é válido ou inválido.

onzenum = False
cpf = (input("dite seu cpf: "))
lista_cpf=[]
cdigito1=0
digito2=0
cont=10
for numero in cpf:
    cdigito1+=(cont*int(numero))
    print(numero)
    #print(digito1)
    cont-=1
print(cdigito1)  


if cdigito1%11<2:
    digito1=0
else:
    digito1=11-(cdigito1%11)      
    
print(digito1)
