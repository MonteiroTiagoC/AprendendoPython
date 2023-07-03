altura = float(input('Insira a altura da parede: '))
largura = float(input('Insira a largura da parede: '))

area = altura*largura
qtd_tinta = area/2

print(f'A área é {area:.2f}m2 e a quantidade de tinta necessária é {qtd_tinta}L')