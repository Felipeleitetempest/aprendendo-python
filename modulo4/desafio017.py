'''ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
hi = (ca ** 2 + co ** 2) ** (1/2)
print('O comprimento da hipotenusa é: {}'.format(hi))'''

from math import hypot
ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
hi = hypot(ca, co)
print('O comprimento da hipotenusa é: {}'.format(hi))
