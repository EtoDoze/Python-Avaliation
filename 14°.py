# Crie um programa que idenTfique se uma palavra é um palíndromo

def verificar_palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False
resultado = verificar_palindromo(str(input("escolhe a palavra:")))
print(resultado)