import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root' ,
    password = 'root',
    database = 'loja'
)

cursor = db.cursor()

#create
db_nome = 'loja'
create = f'CREATE DATABASE {db_nome}'

#create table
table = 'CREATE TABLE funcionarios(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nome VARCHAR(50), salario FLOAT)'

#insert
insert = 'INSERT INTO funcionarios (nome, salario) VALUES ("Ronaldo", "1200.00"), ("Marcos", "1500.00"), ("Guilherme", "2300.00"), ("Matheus", "7400.00")'

cursor.execute(insert)