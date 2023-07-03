# Calculadora de equação do segundo grau

a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))

delta = b** - (4 * a * c)
x1 = (-b + (delta**(1/2)))/(2 * a)
x2 = (-b - (delta**(1/2)))/(2 * a)

print(f'X1 = {x1} e X2 = {x2}')