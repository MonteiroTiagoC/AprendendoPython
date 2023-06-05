from math import pi
from math import sqrt


#Calcular área de um triângulo

base = float(input("Informe a base do triângulo: "))
altura = float(input("Informe a altura do triângulo: "))

area_triangulo = (base*altura)/2

#Calcular comprimento de um circunferência

raio = float(input("Insira o raio da circunferência: "))

compimento_circ = 2*raio*pi

#Soma e produto

valor_a = float(input("Insira o valor de A: "))
valor_b = float(input("Insira o valor de B: "))

Soma = valor_a + valor_b
Produto = valor_a * valor_b

#Conversão de velocidade média

velocidade_km = float(input("Informe a velocudade média em km/h"))

velocidade_m = velocidade_km * 3.6

#Distância enre dois pontos

x1 = float(input("Insira o valor de x de P1: "))
y1 = float(input("Insira o valor de y de P1: "))
x2 = float(input("Insira o valor de x de P2: "))
y2 = float(input("Insira o valor de y de P2: "))

distancia = sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))

#Bhaskara
#ax^2 + bx + c = 0

var_a = float(input("Insira a variável a: "))
var_b = float(input("Insira a variável b: "))
var_c = float(input("Insira a variável c: "))

delta = pow(var_b, 2) - (4*var_a*var_c)

val_x1 = (-var_b + sqrt(delta)) / (2*var_a)
val_x2 = (-var_b - sqrt(delta)) / (2*var_a)

print(f"Os valores de x são:/n X1 = {val_x1}  X2 = {val_x2}")

#Salário corretor de imóveis

nome_corretor = input("Insia o nome do corretor: ")
qtd_vendas = int(input("Insira a quantidade de vendas deste corretor: "))
total_vendas = float(input("Insira o total das vendas deste corretor: "))

salario = 1500 + qtd_vendas*200 + (total_vendas/100)*5

print(f"O salário final do correor {nome_corretor} é de {salario:.2f} reais.")

#Quanidade de salários mínimos

salario_min = float(input("Insira o saláio mínimo atual: "))
salario_usuario = float(input("Insira seu saláio: "))

qtd_salario = salario_usuario/salario_min

print(f"Você recebe {qtd_salario:.2f} salários mínimos")

#Dois inteiros positivos

num_1 = int(input("Insira um número inteiro positivo: "))
num_2 = int(input("Insira outro número inteiro positivo: "))

cubo_num = pow(num_2, 3)
media_num = sqrt(pow(num_1, 2)*pow(num_2))

print(f"O cudo do segundo número é: {cubo_num} e a média geométrica é {media_num:.2f}")

#Copos de suco (transferência de valores)

copo1 = "laranja"
copo2 = "acelora"

copo_aux = copo1
copo1 = copo2
copo2 = copo_aux

print(f"Copo 1 = {copo1} Copo 2 = {copo2}")

