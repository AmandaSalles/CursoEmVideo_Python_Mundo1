'''
o tal do IF e ELSE
------------------------------
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

#OU

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')

------------------------------

nome = str(input('Qual é o seu nome? '))
if nome == 'Amanda':
    print('Belíssimo nome :D')
else:
    print('que nome normal...')
print('Bom dia {}!'.format(nome))

----------------------------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {}'.format(m))
if m >= 6:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais.')'''

