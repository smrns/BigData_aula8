def calcular_dobro(n):
    n = numero * numero
    return n 


def calcular_quadrado(n):
    n = numero ** numero
    return n


numero = int(input('Digite um número: '))

resultado_dobro = calcular_dobro(numero)
resultado_quadrado = calcular_quadrado(numero)
print(f'O dobro é: {resultado_dobro} \nO quadrado é: {resultado_quadrado}')


