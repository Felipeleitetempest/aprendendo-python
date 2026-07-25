largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('A área da parede é de {}m² e você precisará de {}L de tinta para pintá-la'.format(area, tinta))
