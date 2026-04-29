# Funções - normalmente é no começo do código
def saudacao():
    print('Oi, como vai?')

saudacao()

# for i in range(5):
#     saudacao()

def saudacao(x):
    print(f'Oi, {x}. Como vai?')


nome = 'Sabrina'
saudacao(nome)


# Cálculos
def somar(a, b):
    r = a + b
    print(f'Resposta {r}')


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
somar(n1, n2)




