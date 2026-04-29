def imc(verifica_imc):
    if verifica_imc <= 16.9:
        print('Muito abaixo do peso')
    elif verifica_imc <= 18.4:
        print('Abaixo do peso')





altura = float(input('Qual é sua altura? '))
peso = float(input('Qual é o seu peso? Kg'))
verifica_imc = peso / (altura * altura)