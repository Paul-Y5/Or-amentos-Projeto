import sqlite3 as sql

# Conexão com o banco de dados
conect = sql.connect('banco_Dados.db')

# Tabela Usuário
with conect:
    current = conect.cursor()
    current.execute("CREATE TABLE Usuario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, senha TEXT)")

# Tabela Categoria
with conect:
    current = conect.cursor()
    current.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# Tabela Receita
with conect:
    current = conect.cursor()
    current.execute("CREATE TABLE Receita(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL(10,2))")

# Tabela Gastos
with conect:
    current = conect.cursor()
    current.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL(10,2))")