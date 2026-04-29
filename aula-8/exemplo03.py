def somar(a, b):
    r = a + b
    return r


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

# recebendo o retorno da função
resposta = somar(n1, n2)
print(f'O resultado é: {resposta}')
