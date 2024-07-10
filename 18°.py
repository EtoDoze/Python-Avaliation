# Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o 
#seu perímetro.

altura = int(input("diga altura:"))
base = int(input("diga a base misera:"))

perimetro = altura + base + altura + base
area = base * altura

print("seu perimetro:", perimetro, "sua area:", area)

