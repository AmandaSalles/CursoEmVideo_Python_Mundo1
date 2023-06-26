from random import randint
from time import sleep
pc = randint(0,5)
print('\033[0;30;45m➶➴\033[m' * 17)
print('\033[0;36mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[0;30;45m➶➴\033[m' * 17)
player = int(input('Em que número eu pensei?'))
print('Processando...')
sleep(3)
if player == pc:
    print('Parabéns! você acertou! ◝₍ᵔᵕᵔ₎◜')
else:
    print('Ganhei! Eu pensei no número {}, e não no número {}! ₍ ๑ ˃ᴗ˂₎و '.format(pc, player))

