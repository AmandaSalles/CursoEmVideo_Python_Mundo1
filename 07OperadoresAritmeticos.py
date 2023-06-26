#5+2 ==
#5-2 ==
#5*2 ==
#5/2 ==
#5**2 ==
#5//2 ==
#5%2 ==

# ordem de precedência:
# 1º - ()
# 2º - **
# 3º - *, /, //, %
# 4º - +, -

#------------------------------------
#nome = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:^20} !'.format(nome))


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {}, e a divisão é {:.2f},'.format(s, m, d), end='')
print('divisão inteira é {} e potência é {}'.format(di, e))


