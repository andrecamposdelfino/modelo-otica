import sqlite3

conexao = None
cursor = None

try:
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()

    tabela_cliente = """

        create table if not exists cliente(
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT NOT NULL,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            email TEXT NOT NULL
        )

    """
    cursor.execute(tabela_cliente)
    conexao.commit()

    tabela_fornecedor = """

        create table if not exists fornecedor(
            id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_fornecedor TEXT NOT NULL,
            contato TEXT NOT NULL,
            endereco TEXT NOT NULL
        )

    """
    cursor.execute(tabela_fornecedor)
    conexao.commit()

    tabela_produto = """

        create table if not exists produto(
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_produto TEXT NOT NULL,
            tpo TEXT NOT NULL,
            preco DECIMAL (10, 2),
            id_fornecedor INTEGER,
            FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (id_fornecedor)
        )

    """
    cursor.execute(tabela_produto)
    conexao.commit()


    tabela_funcionario = """

        create table if not exists funcionario(
            id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            salario DECIMAL (10, 2)
        )

    """
    cursor.execute(tabela_funcionario)
    conexao.commit()

    tabela_pedido = """
        create table if not exists pedido(
            id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
            data_pedido DATE,
            id_cliente INTEGER,
            id_funcionario INTEGER,
            FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
            FOREIGN KEY (id_funcionario) REFERENCES funcionario (id_funcionario)

        )

    """
    cursor.execute(tabela_pedido)
    conexao.commit()

    tabela_item_pedido = """
        create table if not exists itempedido(
            id_item INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pedido INTEGER,
            id_produto INTEGER,
            quantidade INTEGER,
            preco_unitario DECIMAL (10, 2),
            FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
            FOREIGN KEY (id_produto) REFERENCES funcionario (id_produto)
        )

    """
    cursor.execute(tabela_item_pedido)
    conexao.commit()


except Exception as error:
    print(f"Erro ao tentar criar a tabela  : {error}")