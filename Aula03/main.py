from datetime import datetime
data_atual = datetime.now()

nome_aluno = input("Digite seu nome: ")
idade_aluno = int(input("Insia sua idade: "))
curso = input("Digite seu curso: ")

print(f"O aluno {nome_aluno} possui {idade_aluno} anos e está cursando {curso}.")
print(f"Acessado em: {data_atual}")