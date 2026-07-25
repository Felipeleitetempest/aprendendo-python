P = float(input('Digite o preço do produto:R$ '))
novoP = P - (P * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(P, novoP))
