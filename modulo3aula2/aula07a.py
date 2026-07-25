n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1+n2
m = n1-2
d = n1/n2
e = n1**n2
di = n1//n2
print('A soma é {},  \na subtração é {}, \na divisão é {:.3f}'.format(s, m, d), end=" ")
print('A potência é {}, e a divisão inteira é {}'.format(e, di))
