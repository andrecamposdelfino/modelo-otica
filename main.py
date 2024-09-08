
import database
from modelo import Cliente, Funcionario, Fornecedor, Produto, Pedido, ItensPedido

conn = database.conexao
conn.execute("PRAGMA foreign_keys=ON")
cursor = database.cursor

cliente = Cliente(None, "98952137321", "Janne Mary", "Av Euclides Paulino", "jannemary.ac@gmail.com")
funcionario = Funcionario(None, "Ana Celia", "Analista Financiero", 3900.00)
fornecedor = Fornecedor(None, "Chilebeans", "11 991457571", "Av Carapinima")
produto = Produto(None, "Oculos diversos", "Oculos", 160.99, 2)
pedido = Pedido(None, "2024-09-08", 2, 1)
item_pedido = ItensPedido(None, 1, 1, 2, 560.99)


# ITEM PEDIDO
def inserir_item_pedido(item_pedido):
    query = "INSERT INTO itempedido VALUES(:id_item, :id_pedido, :id_produto, :quantidade, :preco_unitario)"
    cursor.execute(query, vars(item_pedido))
    conn.commit()
    conn.close()


# PEDIDO
def inserir_pedido(pedido):
    query = "INSERT INTO pedido VALUES(:id_pedido, :data_pedido, :id_cliente, :id_funcionario)"
    cursor.execute(query, vars(pedido))
    conn.commit()
    conn.close()

# CLIENTE
def inserir_cliente(cliente):
    query = "INSERT INTO cliente VALUES(:id_cliente, :cpf, :nome, :endereco, :email)"
    cursor.execute(query, vars(cliente))
    conn.commit()
    conn.close()

# FUNCIONARIO
def inserir_funcionario(funcionario):
    query = "INSERT INTO funcionario VALUES(:id_funcionario, :nome, :cargo, :salario)"
    cursor.execute(query, vars(funcionario))
    conn.commit()
    conn.close()


# FORNECEDOR
def inserir_fornecedor(fornecedor):
    query = "INSERT INTO fornecedor VALUES(:id_fornecedor, :nome_fornecedor, :contato, :endereco)"
    cursor.execute(query, vars(fornecedor))
    conn.commit()
    conn.close()



# PRODUTO
def inserir_produto(produto):
    query = "INSERT INTO produto VALUES(:id_produto, :nome_produto, :tipo, :preco, :id_fornecedor)"
    cursor.execute(query, vars(produto))
    conn.commit()
    conn.close()

def atulaiza_produto(nome_produto, tipo, preco, id_fornecedor, id):
    query = f"UPDATE produto SET nome_produto = ?, tipo = ?, preco = ?, id_fornecedor = ? WHERE id_produto = ?"
    cursor.execute(query, (nome_produto, tipo, preco, id_fornecedor, id))
    conn.commit()
    conn.close()

# atulaiza_produto("Oculos de grau multifocal", "Oculos", 760.99, 1, 1)





