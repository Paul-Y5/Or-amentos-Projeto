import sqlite3 as sql

# Conexão com o banco de dados
conexao = sql.connect('banco_Dados.db')

#Inserir dados
def inserir_usuario(nome, email, senha):
    with conexao:
        current = conexao.cursor()
        current.execute("INSERT INTO Usuario(nome, email, senha) VALUES(?, ?, ?)", (nome, email, senha))

def inserir_categoria(nome):
    with conexao:
        current = conexao.cursor()
        current.execute("INSERT INTO Categoria(nome) VALUES(?)", (nome,))

def inserir_receita(categoria, adicionado_em, valor):
    with conexao:
        current = conexao.cursor()
        current.execute("INSERT INTO Receita(categoria, adicionado_em, valor) VALUES(?, ?, ?)", (categoria, adicionado_em, valor))

def inserir_gastos(categoria, retirado_em, valor):
    with conexao:
        current = conexao.cursor()
        current.execute("INSERT INTO Gastos(categoria, retirado_em, valor) VALUES(?, ?, ?)", (categoria, retirado_em, valor))

#Listar dados
def listar_usuarios():
    with conexao:
        current = conexao.cursor()
        current.execute("SELECT * FROM Usuario")
        return current.fetchall()
    
def listar_categorias():
    with conexao:
        current = conexao.cursor()
        current.execute("SELECT * FROM Categoria")
        return current.fetchall()

def listar_receitas():
    with conexao:
        current = conexao.cursor()
        current.execute("SELECT * FROM Receita")
        return current.fetchall()
    
def listar_gastos():
    with conexao:
        current = conexao.cursor()
        current.execute("SELECT * FROM Gastos")
        return current.fetchall()

#Deletar dados
def deletar_usuario(id):
    with conexao:
        current = conexao.cursor()
        current.execute("DELETE FROM Usuario WHERE id=?", (id,))

def deletar_categoria(id):
    with conexao:
        current = conexao.cursor()
        current.execute("DELETE FROM Categoria WHERE id=?", (id,))

def deletar_receita(id):
    with conexao:
        current = conexao.cursor()
        current.execute("DELETE FROM Receita WHERE id=?", (id,))

def deletar_gastos(id):
    with conexao:
        current = conexao.cursor()
        current.execute("DELETE FROM Gastos WHERE id=?", (id,))

#Atualizar dados
def atualizar_usuario(id, nome, email, senha):
    with conexao:
        current = conexao.cursor()
        current.execute("UPDATE Usuario SET nome=?, email=?, senha=? WHERE id=?", (nome, email, senha, id))

def atualizar_categoria(id, nome):
    with conexao:
        current = conexao.cursor()
        current.execute("UPDATE Categoria SET nome=? WHERE id=?", (nome, id))

def atualizar_receita(id, categoria, adicionado_em, valor):
    with conexao:
        current = conexao.cursor()
        current.execute("UPDATE Receita SET categoria=?, adicionado_em=?, valor=? WHERE id=?", (categoria, adicionado_em, valor, id))

def atualizar_gastos(id, categoria, retirado_em, valor):
    with conexao:
        current = conexao.cursor()
        current.execute("UPDATE Gastos SET categoria=?, retirado_em=?, valor=? WHERE id=?", (categoria, retirado_em, valor, id))

#Fechar conexão
def fechar_conexao():
    conexao.close()

#Teste
"""if __name__ == '__main__':
    inserir_usuario('João', 'jp@tt.pt', '123')
    inserir_categoria('Alimentação')
    inserir_receita('Alimentação', '2021-06-01', 100.00)
    inserir_gastos('Alimentação', '2021-06-01', 50.00)
    print(listar_usuarios())
    print(listar_categorias())
    print(listar_receitas())
    print(listar_gastos())

    atualizar_usuario(1, 'João Pedro', 'jp@ua.pt', '1234')
    atualizar_categoria(1, 'Transporte')
    atualizar_receita(1, 'Transporte', '2021-06-01', 200.00)
    print(listar_usuarios())
    print(listar_categorias())
    print(listar_receitas())
    print(listar_gastos())

    deletar_usuario(1)
    deletar_categoria(1)
    deletar_receita(1)
    deletar_gastos(1)
    print(listar_usuarios())
    print(listar_categorias())
    print(listar_receitas())
    print(listar_gastos())

    fechar_conexao()"""