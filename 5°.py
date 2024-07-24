#5) Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3%
#ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de
#2% ao ano, escreva um programa, que imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.

A = 5000000
B = 7000000

A_nat = A * 0.03
B_nat = B * 0.02
cont = 0

while A < B:
    cont =+ 1
    A = A - A_nat
    B = B - B_nat

print(f"A população de A é:{A} e a de B é:{B}")