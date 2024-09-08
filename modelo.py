class Cliente:
    def __init__(self, id_cliente, cpf, nome, endereco, email):
        self.id_cliente = id_cliente #chave primaria
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.email = email

class Produto:
    def __init__(self, id_produto, nome_produto, tipo, preco, id_fornecedor):
        self.id_produto = id_produto # chave primaria
        self.nome_produto = nome_produto
        self.tipo = tipo #ex oculos, lente
        self.preco = preco
        self.id_fornecedor = id_fornecedor # chave estrageira

class Fornecedor:
    def __init__(self, id_fornecedor, nome_fornecedor, contato, endereco):
        self.id_fornecedor = id_fornecedor # chave primaria
        self.nome_fornecedor = nome_fornecedor
        self.contato = contato
        self.endereco = endereco

class Pedido:
    def __init__(self, id_pedido, data_pedido, id_cliente, id_funcionario):
        self.id_pedido = id_pedido  # chave primaria
        self.data_pedido = data_pedido
        self.id_cliente = id_cliente # chave estrageira referenciando a tabela cliente
        self.id_funcionario = id_funcionario # chave estrageira referenciando a tabela funcionario

class ItensPedido:
    def __init__(self, id_item, id_pedido, id_produto, quantidade, preco_unitario):
        self.id_item = id_item # chave primaria
        self.id_pedido = id_pedido # chave estrangeira referenciando a tabela pedido
        self.id_produto = id_produto # chave estrangeira referenciando a tabela produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

class Funcionario:
    def __init__(self, id_funcionario, nome, cargo, salario):
        self.id_funcionario = id_funcionario # chave primaria
        self.nome = nome
        self.cargo = cargo
        self.salario = salario