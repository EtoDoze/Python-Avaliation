#Construa um algoritmo que, tendo como dados de entrada dois pontos
#quaisquer no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles.
#A fórmula que efetua tal cálculo é: 


def calcular_distancia(x1, y1, x2, y2):
    # Calcula a diferença entre as coordenadas
    delta_x = x2 - x1
    delta_y = y2 - y1

    # Calcula o quadrado das diferenças
    delta_x2 = delta_x * delta_x
    delta_y2 = delta_y * delta_y

    # Soma os quadrados das diferenças
    soma = delta_x2 + delta_y2

    # Função para calcular a raiz quadrada manualmente (aproximação)
    def raiz_quadrada(n):
        # Aproximação inicial
        r = n
        # Melhorando a aproximação
        precision = 0.00001  # precisão desejada
        while abs(n - r * r) > precision:
            r = (r + n / r) / 2
        return r

    # Calcula a raiz quadrada da soma
    distancia = raiz_quadrada(soma)

    return distancia

# Exemplo de uso:
x1 = int(input("Escolha x1: "))
y1 = int(input("Escolha y1: "))
x2 = int(input("Escolha x2: "))
y2 = int(input("Escolha y2: "))
distancia = calcular_distancia(x1, y1, x2, y2)
print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é {distancia:.4f}")