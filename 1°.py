##Faça um programa que calcule o fatorial de todos os numeros impares dentre os 10 primeiros da sequência de Fibonacci.

def fibonacci_iterativo(n):
    a, b = 1, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Digite o número de termos desejado: "))
fibonacci_iterativo(n)

