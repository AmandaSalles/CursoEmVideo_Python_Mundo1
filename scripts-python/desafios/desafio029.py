#quando usamos apenas o IF, é chamado de CONDIÇÃO SIMPLES

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80km/h.')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))

print('Tenha um bom dia! Dirija em segurança! 🚙')