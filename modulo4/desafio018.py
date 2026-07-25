from math import radians, sin, cos, tan
a = float(input('Digite o angulo que você deseja: '))
a = radians(a)
print('O seno de {} é: {:.2f}'.format(a, sin(a)))
print('O cosseno de {} é: {:.2f}'.format(a, cos(a)))
print('A tangente de {} é: {:.2f}'.format(a, tan(a)))