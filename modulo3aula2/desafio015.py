kmsrodados = float(input('Quantos km foram rodados com o carro? '))
diasalugado = int(input('Por quantos dias o carro foi alugado? '))
preco = (diasalugado*60) + (kmsrodados*0.15)
print('O total a pagar é de R${:.2f}'.format(preco))
