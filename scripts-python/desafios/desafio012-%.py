#numero * a porcentagem / 100

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto vai custar R${:.2f}'.format(preço, novo))

