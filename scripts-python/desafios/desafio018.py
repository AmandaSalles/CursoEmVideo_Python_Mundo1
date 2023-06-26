import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo {} tem o SENO de {:.2f}.'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}.'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tangente))


#OU usar > from math import radians, sin, cos, tan< , e remover todas as referências a >MATH.<