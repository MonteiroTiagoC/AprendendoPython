preco = float(input('Insira o preço do produto: '))

disc = preco - ((preco/100)*5)
print(f'O preço com desconto é: {disc:.2f} reais')