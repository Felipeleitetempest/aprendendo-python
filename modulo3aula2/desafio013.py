salario = float(input('Digite o salário do funcionário:R$ '))
novoS = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com o aumento de 15% vai passar a ganhar R${:.2f}'.format(salario, novoS))
