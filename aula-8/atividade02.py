# Crie um algoritmo que: receba o peso total de peixe pescados no dia
# verifique se houve excesso
# calcule e retorne o valor da multa(se houver)
# mostre a mensagem correspondente na tela

def verificar_kg(peso_total):
    limite_diario = 100 #Kg
    multa_por_kg = 4.00 #Reais

    if peso_total > limite_diario:
        excesso = peso_total - limite_diario
        multa = excesso * multa_por_kg
        print(f'Atenção! Você excedeu o limite em {excesso:.2f} kg.')
        print(f'O valor da multa a pagar é: R$ {multa:.2f}')
        return multa
    else:
        print('Peso dentro do limite permitido. Não há multa.')
        return 0


peso_pescado = float(input('Digite o peso total de peixes (kg): '))
valor_da_multa = verificar_kg(peso_pescado)